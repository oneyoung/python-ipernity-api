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

    def get_auth_url(self, frob=None):
        ''' get auth url

        If optional paramter 'frob' provided, will return frob auth url
        '''
        params = {}
        params['api_key'] = self.api_key
        params.update(self.perms)
        if frob:
            params['frob'] = frob
        # auth url need api_sig
        query = urllib.urlencode(params)
        api_sig = rest.sign_keys(self.api_secret, query)
        query += '&api_sig=%s' % api_sig
        # composite url
        url = USER_AUTH_URL + '?' + query
        return url

    def get_frob_auth_url(self):
        ''' get auth_url with frob

        return (auth_url, frob)
        '''
        resp = rest.call_api('auth.getFrob',
                             api_key=self.api_key,
                             api_secret=self.api_secret,
                             signed=True)
        # TODO: should we create a AUTH object here
        frob = resp['auth']['frob']
        self.frob = frob

        return self.get_auth_url(frob), frob
