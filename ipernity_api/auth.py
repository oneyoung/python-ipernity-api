'''
Applications can request permissions on the following items:

    Photos/video/docs: permissions for photos/videos/docs posted.
    Articles: permissions for articles.
    Contact: permissions on the contacts.
    Profile: permissions on the user's profile.

    The requested permission can be:
        read : grants read-only access to user's items, even private.
        write : permits the modification of the user's items (and also grants read permission.).
        delete : permits the deletion of the user's items (and also grants write and read permission.).


A connection URL is built like this:
http://www.ipernity.com/apps/authorize?api_key=[api_key]&perm_X=[perm]&api_sig=[api_sig]
    [api_key] : your API key.
    [api_sig] : this request signature built using your secret.
    [perm_doc] : the requested permission for photos/videos/docs. (read/write/delete).
    [perm_blog] : the requested permission for articles. (read/write/delete).
    [perm_network] : the requested permission for the contacts (read/write/delete).
    [perm_profile] : the requested permission for the user's profile (read/write).

In the case of an authentication request for a desktop application, a frob parameter will have to be added.
http://www.ipernity.com/apps/authorize?api_key=[api_key]&perm_X=[perm]&frob=[frob]&api_sig=[api_sig]

'''
import urllib
from . import keys
from . import rest

REQUEST_TOKEN_URL = 'http://www.ipernity.com/apps/oauth/request'
USER_AUTH_URL = 'http://www.ipernity.com/apps/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.ipernity.com/apps/oauth/access'


class AuthError(Exception):
    pass


class AuthHandler(object):
    def __init__(self, api_key=None, api_secret=None, perms=None):
        '''
        Parameters:
            perms: is a dict consist of 'perm_xxx': 'read/write/delete'
                perm_xxx can be: perm_doc, perm_blog, perm_network, perm_profile
        '''
        self.api_key = api_key or keys.API_KEY
        self.api_secret = api_secret or keys.API_SECRET
        if not self.api_key or not self.api_secret:
            raise AuthError('No api_key or api_secret given')

        if perms:  # sanity check for permissions
            perm_types = ['perm_doc', 'perm_blog', 'perm_network', 'perm_profile']
            perm_modes = ['read', 'write', 'delete']
            for k in perms.keys():
                if k not in perm_types:
                    raise AuthError('Unknown permission type: %s' % k)
                if perms[k] not in perm_modes:
                    raise AuthError('Unknown permission mode %s for %s' % (perms[k], k))
        self.perms = perms

        self.frob = None

    def get_auth_url(self):
        ''' get auth url

        this method need to be overrided
        '''

    def compose_url(self, **kwarg):
        ''' compose url for auth

        parameters:
            **kwarg: additional parameters can be provided,
                for example: frob, callback
        '''
        params = {}
        params['api_key'] = self.api_key  # add api_key
        params.update(self.perms)  # append permissions
        params.update(kwarg)  # additional parameters
        # auth url need api_sig
        query = urllib.urlencode(params)
        api_sig = rest.sign_keys(self.api_secret, query)
        query += '&api_sig=%s' % api_sig
        # composite url
        url = USER_AUTH_URL + '?' + query
        return url


class WebAuthHanlder(AuthHandler):
    '''WebAuthHanlder: auth class for web application

    Steps:
        1. Redirect the user to the authentication page
        2. Get back the frob
        3. Exchange the frob for a token

    Note: web callback URL is registered in ipernity.com
    when applying for API key
    (Authentication method: Web)

    Once authenticated, the member (its browser) is automatically
    redirected to your callback URL with the frob parameter.
    For example: http://www.yoursite.com/callback.php?frob=123456789-0ad5e2a8
    This frob is a disposable one-time use authentication ticket.
    This ticket remains valid for a few minutes only and must be exchanged
    for an auth_token authentication token .
    '''
    def get_auth_url(self):
        return self.compose_url()


class DesktopAuthHandler(AuthHandler):
    '''DesktopAuthHandler: auth class for non-web application which has no callback.
    '''
    def __init__(self, *args, **kwarg):
        AuthHandler.__init__(self, *args, **kwarg)
        # get frob
        resp = rest.call_api('auth.getFrob',
                             api_key=self.api_key,
                             api_secret=self.api_secret,
                             signed=True)
        # TODO: should we create a AUTH object here
        frob = resp['auth']['frob']
        self.frob = frob

    def get_auth_url(self):
        return self.compose_url(frob=self.frob)

import urlparse
import random
import time


def escape(s):
    """Escape a URL including any /."""
    return urllib.quote(s, safe='~')


def _utf8_str(s):
    """Convert unicode to utf-8."""
    if isinstance(s, unicode):
        return s.encode("utf-8")
    else:
        return str(s)


def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


def generate_timestamp():
    """Get seconds since epoch (UTC)."""
    return str(int(time.time()))


class OAuthAuthHandler(AuthHandler):
    def __init__(self, callback=None, *arg, **kwarg):
        AuthHandler.__init__(self, *arg, **kwarg)
        self.callback = callback
        self.verified = False
        # first get a oauth token
        self._request(REQUEST_TOKEN_URL)

    @staticmethod
    def _normalized_parameters(params):
        """Return a string that contains the parameters that must be signed."""
        try:
            # Exclude the signature if it exists.
            del params['oauth_signature']
        except:
            pass
        # Escape key values before sorting.
        key_values = [(escape(_utf8_str(k)), escape(_utf8_str(v)))
                      for k, v in params.items()]
        # Sort lexicographically, first after key, then after value.
        key_values.sort()
        # Combine key value pairs into a string.
        return '&'.join(['%s=%s' % (k, v) for k, v in key_values])

    def _build_signature(self, url, params, token=None):
        ''' signature OAuth request '''
        # private key to signature
        # consist of "consumer secret&token secret"
        key = '%s&' % escape(self.api_secret)
        if token:
            key += escape(token)
        # string to be signed consist of 3 parts:
        # 1. HTTP request method, uppercase, i.e. HEAD, GET, POST
        # 2. request URL
        # 3. normalized request parameters
        # Each item is encoded and separated by an '&' character
        sig = ('GET',
               url,
               self._normalized_parameters(params))
        raw = '&'.join(map(escape, sig))
        # HMAC object.
        import hmac
        import binascii

        try:
            import hashlib  # 2.5
            hashed = hmac.new(key, raw, hashlib.sha1)
        except:
            import sha  # Deprecated
            hashed = hmac.new(key, raw, sha)

        # Calculate the digest base 64.
        return binascii.b2a_base64(hashed.digest())[:-1]

    def _request(self, url, verify=False):
        ''' fire the request to url, and save the oauth token

        if token given, this is a access token verify request.
        '''
        params = {
            'oauth_consumer_key': self.api_key,
            'oauth_signature_method': 'HMAC-SHA1',
            'oauth_timestamp': generate_timestamp(),
            'oauth_nonce': generate_nonce(),
        }
        # callback is not needed when do verify
        if self.callback and not verify:
            params['oauth_callback'] = self.callback
        if verify:  # verify the oauth_token
            params['oauth_token'] = self.oauth_token
            token_secret = self.oauth_token_secret
        else:
            token_secret = None
        # get signature
        oauth_signature = self._build_signature(url, params, token_secret)
        params['oauth_signature'] = oauth_signature
        # compose URL
        req_url = url + '?' + urllib.urlencode(params)
        # send request and save auth token
        resp = urllib.urlopen(req_url)
        oauth_token_resp = dict(urlparse.parse_qsl(resp.read()))
        self.oauth_token = oauth_token_resp['oauth_token']
        self.oauth_token_secret = oauth_token_resp['oauth_token_secret']

    def get_auth_url(self):
        params = {}
        params['oauth_token'] = self.oauth_token
        params.update(self.perms)
        url = USER_AUTH_URL + '?' + urllib.urlencode(params)
        return url

    def verify(self):
        ''' verify the access token '''
        self._request(ACCESS_TOKEN_URL, verify=True)
        self.verified = True
