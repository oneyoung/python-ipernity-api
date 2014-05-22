from unittest import TestCase
from ipernity_api import auth, rest, errors, ipernity
from .utils import auth_in_browser, auto_auth


class AuthTest(TestCase):
    oauth_file = '/tmp/ipernity_auth_tmp'

    def test_instance_init(self):
        perms = {'doc': 'read'}
        # this should OK
        auth.AuthHandler(perms=perms)
        # wrong perms type should raise exception
        perms['unknown'] = 'unkonwn'
        with self.assertRaisesRegexp(auth.AuthError, 'permission type'):
            auth.AuthHandler(perms=perms)
        perms.pop('unknown')
        # wrong perms mode should also raise exception
        perms['blog'] = 'wrong_mode'
        with self.assertRaisesRegexp(auth.AuthError, 'permission mode'):
            auth.AuthHandler(perms=perms)
        perms.pop('blog')

    def test_get_url(self):
        def test_class(cls):
            perms = {'doc': 'write'}
            handler = cls(perms=perms)
            url = handler.get_auth_url()
            self.assertIsNotNone(url)

        test_class(auth.WebAuthHanlder)
        test_class(auth.DesktopAuthHandler)

    def test_authed_request(self):
        auto_auth()
        ohdlr = auth.AUTH_HANDLER
        auth.set_auth_handler(None)
        # no auth handler should raise exception
        with self.assertRaises(errors.IpernityError):
            rest.call_api('account.getQuota', authed=True)
        # explcit resign should OK
        rest.call_api('account.getQuota',
                      authed=True,
                      auth_handler=ohdlr)
        # set_auth_handler should OK
        auth.set_auth_handler(ohdlr)
        rest.call_api('account.getQuota', authed=True)

    def test_getUser(self):
        auto_auth()
        handler = auth.AUTH_HANDLER
        user = handler.getUser()
        self.assertIsInstance(user, ipernity.User)

    def _test_oauth(self):
        perms = {'doc': 'delete',
                 'blog': 'delete',
                 'network': 'delete', }
        handler = auth_in_browser(auth.OAuthAuthHandler, perms)
        # save handler
        handler.save(self.oauth_file)
        # load handler
        new_hdlr = auth.AuthHandler.load(self.oauth_file)
        self.assertIsNotNone(new_hdlr)

    def _test_desktop_auth(self):
        perms = {'doc': 'write'}
        fpath = self.oauth_file
        #TODO: web said frob is invalid, wired
        handler = auth_in_browser(auth.DesktopAuthHandler, perms)
        # save handler
        handler.save(fpath)
        # load handler
        new_hdlr = auth.AuthHandler.load(fpath)
        self.assertIsNotNone(new_hdlr)
