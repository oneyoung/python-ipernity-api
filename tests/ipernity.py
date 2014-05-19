from unittest import TestCase
from ipernity_api import ipernity


class IpernityTest(TestCase):
    def test_Test(self):
        self.assertEquals('echo', ipernity.Test.echo(echo='echo'))
        self.assertIn('hello', ipernity.Test.hello())
