from unittest import TestCase
from ipernity_api import auth


class AuthTest(TestCase):
    def test_instance_init(self):
        perms = {'perm_doc': 'read'}
        # this should OK
        auth.AuthHandler(perms=perms)
        # wrong perms type should raise exception
        perms['perm_unknown'] = 'unkonwn'
        with self.assertRaisesRegexp(auth.AuthError, 'permission type'):
            auth.AuthHandler(perms=perms)
        perms.pop('perm_unknown')
        # wrong perms mode should also raise exception
        perms['perm_blog'] = 'wrong_mode'
        with self.assertRaisesRegexp(auth.AuthError, 'permission mode'):
            auth.AuthHandler(perms=perms)
        perms.pop('perm_blog')

    def test_get_url(self):
        perms = {'perm_doc': 'write'}
        handler = auth.AuthHandler(perms=perms)
        url = handler.get_auth_url()
        url, frob = handler.get_frob_auth_url()
