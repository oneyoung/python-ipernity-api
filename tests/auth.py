from unittest import TestCase
from ipernity_api import auth


class AuthTest(TestCase):
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

    def _test_oauth(self):
        perms = {'doc': 'write'}
        auth_in_browser(auth.OAuthAuthHandler, perms)


def auth_in_browser(auth_cls, perms):
    ''' OAuth in Browser and return auth object
    Implement:
        1. oauth support url redirect after auth done
        2. we can setup a HTTP server to get such token
    '''
    port = 5678
    redirt_url = "http://localhost:%s" % port

    # get auth url
    auth_handler = auth_cls(callback=redirt_url, perms=perms)
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
            print q
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
