import datetime
from unittest import TestCase
from ipernity_api import ipernity
from . import utils


class IpernityTest(TestCase):
    def __init__(self, *arg, **kwargs):
        TestCase.__init__(self, *arg, **kwargs)
        utils.auto_auth()

    def test_Test(self):
        self.assertEquals('echo', ipernity.Test.echo(echo='echo'))
        self.assertIn('hello', ipernity.Test.hello())

    def test_User(self):
        user_id = 787135
        # get user test
        user = ipernity.User.get(user_id=user_id)
        self.assertIsInstance(user, ipernity.User)
        # filed test
        self.assertIsInstance(user.is_online, bool)
        self.assertIsInstance(user.is_closed, bool)
        # count test
        self.assertIsInstance(user.count['network'], int)
        self.assertIsInstance(user.dates['member_since'], datetime.datetime)

        # quota test
        quota = user.getQuota()
        self.assertIsInstance(quota.is_pro, bool)
        left = quota.upload['used']['mb']
        self.assertIsInstance(left, int)
