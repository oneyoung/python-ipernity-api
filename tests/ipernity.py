from unittest import TestCase
from ipernity_api import ipernity


class IpernityTest(TestCase):
    def test_Test(self):
        self.assertEquals('echo', ipernity.Test.echo(echo='echo'))
        self.assertIn('hello', ipernity.Test.hello())

    def test_User(self):
        user_id = 787135
        # get user test
        user = ipernity.User.get(user_id=user_id)
        self.assertIsInstance(user, ipernity.User)
        # quota test
        quota = user.getQuota()
        left = quota['upload']['used']['mb']
        self.assertIsInstance(left, int)
