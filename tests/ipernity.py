import datetime
from unittest import TestCase
from ipernity_api import ipernity, errors
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
        self.assertIsInstance(user.is_pro, bool)
        # count test
        self.assertIsInstance(user.count['network'], int)
        self.assertIsInstance(user.dates['member_since'], datetime.datetime)

        # quota test
        quota = user.getQuota()
        self.assertIsInstance(quota.is_pro, bool)
        left = quota.upload['used']['mb']
        self.assertIsInstance(left, int)

    def test_Album(self):
        album = ipernity.Album.create(title='This is a album')
        # fields validation
        self.assertIsInstance(album.count['docs'], int)
        self.assertIsInstance(album.dates['created_at'], datetime.datetime)

        # edit test
        new_title = 'New title'
        new_desc = 'This is a new description'
        album.edit(title=new_title, description=new_desc)
        self.assertEquals(album.title, new_title)
        self.assertEquals(album.description, new_desc)

        album_id = album.album_id
        # new album can be get
        album = ipernity.Album.get(album_id=album_id)
        album.delete()
        # after delete, album shoult not found
        with self.assertRaisesRegexp(errors.IpernityAPIError, 'Album not found'):
            ipernity.Album.get(album_id=album_id)
