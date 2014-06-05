import os
import urllib
import urllib2
import json
import hashlib
from .errors import IpernityError, IpernityAPIError
from .multipart import posturl
from . import keys


def _clean_params(params):
    for k, v in params.items():
        if isinstance(v, bool):
            params[k] = 1 if v else 0
    return params


def call_api(api_method, api_key=None, api_secret=None, signed=False,
             authed=False, http_post=True, auth_handler=None, **kwargs):
    ''' file request to ipernity API

    Parameters:
        method: The API method you want to call
        signed: if request need to add signature
        authed: if user auth needed
        auth_handler: auth_handler
        http_post: if set True, would use POST method, otherwise, GET
            some methods only support GET request, for example: api.methods.get

    Default:
        * always send request with POST method
        * format is JSON
    '''
    # api_keys handling
    if not api_key:
        api_key = keys.API_KEY
    if not api_secret:
        api_secret = keys.API_SECRET
    if not api_key or not api_secret:
        raise IpernityError('No Ipernity API keys been set')
    kwargs['api_key'] = api_key
    kwargs = _clean_params(kwargs)

    url = "http://api.ipernity.com/api/%s/%s" % (api_method, 'json')

    from . import auth
    auth_handler = auth_handler or auth.AUTH_HANDLER
    if authed and not auth_handler:
        raise IpernityError('no auth_handler provided')
    elif auth_handler:
        if isinstance(auth_handler, auth.OAuthAuthHandler):
            kwargs = auth_handler.sign_params(url, kwargs, http_post)
    else:
        if signed:  # signature handling
            api_sig = sign_keys(api_secret, kwargs, api_method)
            kwargs['api_sig'] = api_sig
    data = urllib.urlencode(kwargs)

    # send the request
    try:
        # we use urllib2 here, since urllib has some problem when response is
        # over 8k size
        if http_post:  # POST
            if 'file' in kwargs:  # upload file handling
                fpath = kwargs['file']
                files = [('file', os.path.basename(fpath),
                          open(fpath, 'rb').read())]
                resp_raw = posturl(url, kwargs.items(), files)
            else:
                resp_raw = urllib2.urlopen(url, data).read()
        else:  # GET
            url += '?' + data
            resp_raw = urllib2.urlopen(url).read()
    except Exception, e:
        raise IpernityError(str(e))

    # parse the result
    try:
        resp = json.loads(resp_raw)
    except ValueError, e:
        raise IpernityError('Json decode error at: %s WITH Payload:\n%s'
                            % (str(e), resp_raw))
    # check the response, if error happends, raise exception
    api = resp['api']
    if api['status'] == 'error':
        err_mesg = api['message']
        # add more info to err_mesg
        err_mesg += '\nAPI: %s \nPayload: %s' % (api_method, data)
        err_code = int(api['code'])
        raise IpernityAPIError(err_code, err_mesg)

    return resp


def sign_keys(api_secret, kwargs, method=None):
    ''' request signature: Some API methods require signature.
    Support Request signature and Authorization link signature

    Parameters:
        api_secret: api_secret key
        kwargs: api parameters to be signed
        method: if provided, request signature, otherwise auth link signature

    The request signature corresponds to the md5 of a string
    composed of the following parameters concatenated
    each other without spaces:
        alphabetical ordered parameters followed by their values,
        the called method, (for Request Signature)
        your API key secret.

    Note: kwargs would be sorted in alphabetical order when convert to string
    '''
    param_keys = kwargs.keys()
    param_keys.sort()
    sig_str = ''.join(['%s%s' % (k, kwargs[k]) for k in param_keys])
    # append method & api_secret
    sig_str = sig_str + (method if method else '') + api_secret
    api_sig = hashlib.md5(sig_str).hexdigest()
    return api_sig
