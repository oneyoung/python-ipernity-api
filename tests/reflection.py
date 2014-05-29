from ipernity_api.reflection import call, static_call
from ipernity_api.errors import IpernityError
from unittest import TestCase


class ReflectionTest(TestCase):
    def test_call_decorator(self):
        class Testing:
            @call('test.echo')
            def echo(self, *args, **kwargs):
                return kwargs, lambda k: k['echo']

            @call('test.hello')
            def hello(self, *args, **kwargs):
                return kwargs, lambda k: k['hello']

        t = Testing()
        self.assertEquals('hello', t.echo(echo='hello'))
        self.assertIn('hello', t.hello())

    def test_static_call_decorator(self):
        class Testing:
            @static_call('test.hello')
            def hello(*args, **kwargs):
                return kwargs, lambda k: k['hello']

        self.assertIn('hello', Testing.hello())

    def test_required_parameters(self):
        class Test:
            @call('album.get')
            def test(self, **kwargs):
                return kwargs, lambda k: k['echo']

            @static_call('album.get')
            def static_test(**kwargs):
                return kwargs, lambda k: k['echo']

        # required paramters checking
        with self.assertRaisesRegexp(IpernityError, 'missing'):
            Test.static_test()
        t = Test()
        with self.assertRaisesRegexp(IpernityError, 'missing'):
            t.test()
