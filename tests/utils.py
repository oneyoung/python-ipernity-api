import os
import sys
import unittest
from ipernity_api import auth


class TestCaseError(Exception):
    pass

if sys.version >= '2.7':
    TestCase = unittest.TestCase  # just by pass
elif sys.version >= '2.6':
    # add missing methods of unittest.TestCase in Python2.6
    import re

    class _AssertRaisesContext(object):
        """A context manager used to implement
        TestCase.assertRaises* methods."""

        def __init__(self, expected, test_case, expected_regexp=None):
            self.expected = expected
            self.failureException = test_case.failureException
            self.expected_regexp = expected_regexp

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, tb):
            if exc_type is None:
                try:
                    exc_name = self.expected.__name__
                except AttributeError:
                    exc_name = str(self.expected)
                raise self.failureException(
                    "{0} not raised".format(exc_name))
            if not issubclass(exc_type, self.expected):
                # let unexpected exceptions pass through
                return False
            self.exception = exc_value  # store for later retrieval
            if self.expected_regexp is None:
                return True

            expected_regexp = self.expected_regexp
            if isinstance(expected_regexp, basestring):
                expected_regexp = re.compile(expected_regexp)
            if not expected_regexp.search(str(exc_value)):
                raise self.failureException('"%s" does not match "%s"' %
                         (expected_regexp.pattern, str(exc_value)))
            return True

    class TestCase(unittest.TestCase):
        def assertRaises(self, excClass, callableObj=None, *args, **kwargs):
            """Fail unless an exception of class excClass is raised
               by callableObj when invoked with arguments args and keyword
               arguments kwargs. If a different type of exception is
               raised, it will not be caught, and the test case will be
               deemed to have suffered an error, exactly as for an
               unexpected exception.

               If called with callableObj omitted or None, will return a
               context object used like this::

                    with self.assertRaises(SomeException):
                        do_something()

               The context manager keeps a reference to the exception as
               the 'exception' attribute. This allows you to inspect the
               exception after the assertion::

                   with self.assertRaises(SomeException) as cm:
                       do_something()
                   the_exception = cm.exception
                   self.assertEqual(the_exception.error_code, 3)
            """
            context = _AssertRaisesContext(excClass, self)
            if callableObj is None:
                return context
            with context:
                callableObj(*args, **kwargs)

        def assertRaisesRegexp(self, expected_exception, expected_regexp,
                               callable_obj=None, *args, **kwargs):
            """Asserts that the message in a raised exception matches a regexp.

            Args:
                expected_exception: Exception class expected to be raised.
                expected_regexp: Regexp (re pattern object or string) expected
                        to be found in error message.
                callable_obj: Function to be called.
                args: Extra args.
                kwargs: Extra kwargs.
            """
            context = _AssertRaisesContext(expected_exception,
                                           self, expected_regexp)
            if callable_obj is None:
                return context
            with context:
                callable_obj(*args, **kwargs)

        def assertIsInstance(self, obj, cls, msg=None):
            """Same as self.assertTrue(isinstance(obj, cls)), with a nicer
            default message."""
            if not isinstance(obj, cls):
                standardMsg = '%s is not an instance of %r' % (repr(obj), cls)
                self.fail(self._formatMessage(msg, standardMsg))

        def assertIsNotNone(self, obj, msg=None):
            """Included for symmetry with assertIsNone."""
            if obj is None:
                standardMsg = 'unexpectedly None'
                self.fail(self._formatMessage(msg, standardMsg))

        def assertIn(self, member, container, msg=None):
            """Just like self.assertTrue(a in b), but with a nicer default message."""
            if member not in container:
                standardMsg = '%s not found in %s' % (repr(member),
                                                      repr(container))
                self.fail(self._formatMessage(msg, standardMsg))

else:
    raise TestCaseError('Unsupport python version')


AUTH_FILE_PATH = '.tests.ipernity_auto_auth.tmp'
AUTH_HANDLER = None


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
            # import urlparse
            # p = urlparse.urlparse(self.path)
            # q = urlparse.parse_qs(p.query)
            # auth_token = q['oauth_token'][0]
            # auth_verifier = q['oauth_verifier'][0]
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


def auto_auth():
    global AUTH_HANDLER
    if AUTH_HANDLER:
        return
    if not os.path.exists(AUTH_FILE_PATH):
        perms = {'doc': 'delete',
                 'blog': 'delete',
                 'network': 'delete', }
        handler = auth_in_browser(auth.OAuthAuthHandler, perms)
        # save handler
        handler.save(AUTH_FILE_PATH)
    handler = auth.AuthHandler.load(AUTH_FILE_PATH)
    auth.set_auth_handler(handler)
    AUTH_HANDLER = handler
