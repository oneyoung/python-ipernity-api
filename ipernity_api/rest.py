import urllib
import json
import hashlib
from .errors import IpernityError, IpernityAPIError
from . import keys


def call_api(method, api_key=None, api_secret=None, signed=False, **kwargs):
    ''' file request to ipernity API

    Parameters:
        method: The API method you want to call

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

    data = urllib.urlencode(kwargs)
    if signed:  # signature
        api_sig = sign_keys(api_secret, data, method)
        data += '&api_sig=%s' % api_sig
    url = "http://api.ipernity.com/api/%s/%s" % (method, 'json')
    # send the request
    try:
        resp_raw = urllib.urlopen(url, data).read()
    except Exception, e:
        raise IpernityError(str(e))

    # parse the result
    resp = json.loads(resp_raw)
    # check the response, if error happends, raise exception
    api = resp['api']
    if api['status'] == 'error':
        err_mesg = api['message']
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
