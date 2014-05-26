import urllib
import urllib2
import json
import hashlib
from .errors import IpernityError, IpernityAPIError
from . import keys


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

    url = "http://api.ipernity.com/api/%s/%s" % (api_method, 'json')
    if authed:
        from . import auth
        auth_handler = auth_handler or auth.AUTH_HANDLER
        if not auth_handler:
            raise IpernityError('no auth_handler provided')
        # upload.file and upload.replace both require auth, so put them here
        isupload = kwargs.has_key('file')
        if isupload:
            fname = kwargs.pop('file')  # 'file' should not include in signature
        if isinstance(auth_handler, auth.OAuthAuthHandler):
            kwargs = auth_handler.sign_params(url, kwargs, http_post)
        if isupload:
            kwargs['file'] = open(fname).read()  # add back file
        data = urllib.urlencode(kwargs)
    else:
        data = urllib.urlencode(kwargs)
        if signed:  # signature
            api_sig = sign_keys(api_secret, data, api_method)
            data += '&api_sig=%s' % api_sig
    # send the request
    try:
        # we use urllib2 here, since urllib has some problem when response is
        # over 8k size
        if http_post:  # POST
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
        raise IpernityError('Json decode error at: %s WITH Payload:\n%s' % (str(e), resp_raw))
    # check the response, if error happends, raise exception
    api = resp['api']
    if api['status'] == 'error':
        err_mesg = api['message']
        # add more info to err_mesg
        err_mesg += '\nAPI: %s \nPayload: %s' % (api_method, data)
        err_code = int(api['code'])
        raise IpernityAPIError(err_code, err_mesg)

    return resp


def sign_keys(api_secret, data, method=None):
    ''' request signature: Some API methods require signature.
    Support Request signature and Authorization link signature

    Parameters:
        api_secret: api_secret key
        data: api parameters encode by urlencode
        method: if provided, request signature, otherwise auth link signature

    The request signature corresponds to the md5 of a string
    composed of the following parameters concatenated
    each other without spaces:
        alphabetical ordered parameters followed by their values,
        the called method, (for Request Signature)
        your API key secret.

    Note: must guarantee the order of API parameters, otherwise, md5 would change.
    so we use data already encode by urlencode,
    using dict is not a good idea here, because order of iter might change.
    '''
    # filter out special char '?&='
    sig_str = ''.join(filter(lambda c: c not in '?&=', data))
    # append method & api_secret
    sig_str = sig_str + (method if method else '') + api_secret
    api_sig = hashlib.md5(sig_str).hexdigest()
    return api_sig
