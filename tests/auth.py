import os
from unittest import TestCase
from ipernity_api import auth
from ipernity_api import rest


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
        if not os.path.exists(self.oauth_file):
            self._test_oauth()
        oauth_handler = auth.AuthHandler.load(self.oauth_file)
        rest.call_api('account.getQuota',
                      authed=True,
                      auth_handler=oauth_handler)

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
        fpath = '/tmp/ipernity_auth_tmp'
        #TODO: web said frob is invalid, wired
        handler = auth_in_browser(auth.DesktopAuthHandler, perms)
        # save handler
        handler.save(fpath)
        # load handler
        new_hdlr = auth.AuthHandler.load(fpath)
        self.assertIsNotNone(new_hdlr)


def auth_in_browser(auth_cls, perms):
    ''' OAuth in Browser and return auth object
    Implement:
        1. oauth support url redirect after auth done
        2. we can setup a HTTP server to get such token
    '''
    port = 5678
    redirt_url = "http://localhost:%s" % port

    # get auth url
    if auth_cls is auth.OAuthAuthHandler:
        auth_handler = auth_cls(callback=redirt_url, perms=perms)
    else:
        auth_handler = auth_cls(perms=perms)
    url = auth_handler.get_auth_url()
    # open url in browser
    import webbrowser
    webbrowser.open_new(url)

    # setup a temporary http server to get oath_token
    import BaseHTTPServer

    class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            # parse url to get auth_token
            import urlparse
            p = urlparse.urlparse(self.path)
            q = urlparse.parse_qs(p.query)
            #auth_token = q['oauth_token'][0]
            #auth_verifier = q['oauth_verifier'][0]
            print (q)
            # save back to auth handler
            auth_handler.verify()
            # send response to webpage
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Auth OK. Please close this page.")
            self.wfile.close()

    httpd = BaseHTTPServer.HTTPServer(("", port), Handler)

    httpd.handle_request()  # just handle on request

    return auth_handler
