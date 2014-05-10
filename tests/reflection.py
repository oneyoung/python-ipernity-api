from ipernity_api.reflection import call
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
