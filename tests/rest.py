from unittest import TestCase
from ipernity_api import rest

API_KEY = "2a3f0c090000289F43d4e77eeebe5b92"


class RESTTest(TestCase):
    def test_call_api(self):
        method = 'test.echo'
        echo = 'hello'

        resp = rest.call_api(method, api_key=API_KEY, echo=echo)
        self.assertEquals(resp['echo'], echo)
