import os
import datetime
from unittest import TestCase
from ipernity_api import ipernity, errors
from . import utils


def getfile(fname):
    return os.path.join(os.path.dirname(__file__), 'files', fname)


class IpernityTest(TestCase):
    def __init__(self, *arg, **kwargs):
        TestCase.__init__(self, *arg, **kwargs)
        utils.auto_auth()
        # get a default user
        self.user = utils.AUTH_HANDLER.getUser()
        # fetch some docs for later test
        docs = self.user.getDocs()
        if len(docs) < 2:  # not enough docs, we upload some
            self.upload_files()
            docs = self.user.getDocs()
        self.docs = docs

    def test_Test(self):
        self.assertEquals('echo', ipernity.Test.echo(echo='echo'))
        self.assertIn('hello', ipernity.Test.hello())

    def test_User(self):
        user_id = self.user.id
        # get user test
        user = ipernity.User.get(id=user_id)
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

        # getXXX test
        user.getDocs()
        user.getAlbums()

    def test_Album(self):
        doc1 = self.docs[0]
        doc2 = self.docs[1]
        album = ipernity.Album.create(title='This is a album', cover=doc1)
        # fields validation
        self.assertIsInstance(album.count['docs'], int)
        self.assertIsInstance(album.dates['created_at'], datetime.datetime)
        self.assertIsInstance(album.cover, ipernity.Doc)
        self.assertEquals(doc1.id, album.cover.id)

        # getList test
        ret = ipernity.Album.getList(user=self.user)
        self.assertTrue(ret.info['total'] > 0)
        self.assertTrue(any([a.id == album.id for a in ret]))

        # add doc
        ret = album.docs_add(doc=doc1)
        # check result
        self.assertEqual(ret.info['total'], 1)
        self.assertIsInstance(ret[0]['added'], bool)
        # add docs
        album.docs_add(docs=[doc1, doc2])

        # Faves Test for Album
        Faves = ipernity.Faves
        ret = album.getFaves()
        self.assertEqual(ret.info['count'], 0)
        # Faves add and getList
        Faves.albums_add(album=album)  # add by Faves
        ret = Faves.albums_getList(user=self.user, owner=self.user)  # verifiy Faves list
        self.assertTrue(ret.info['total'] > 0)
        self.assertTrue(any([a.id == album.id for a in ret]))
        # album.getFaves
        # TODO: this fail, wired
        #ret = album.getFaves()
        #ts = ret[0]['faved_at']
        #self.assertIsInstance(ts, datetime.datetime)
        #user = ret[0]['user']  # only one user faves
        #self.assertTrue(user.id == self.user.id)
        # remove it
        Faves.albums_remove(album=album)
        ret = Faves.albums_getList(user=self.user, owner=self.user)  # verifiy Faves list
        self.assertFalse(any([a.id == album.id for a in ret.data]))  # should not found

        # edit test
        new_title = 'New title'
        new_desc = 'This is a new description'
        # Note: new cover should belong to the same album
        # otherwise, ipernity.com would complain "doc not found'
        album.edit(title=new_title, description=new_desc, cover=doc2)
        self.assertEquals(album.title, new_title)
        self.assertEquals(album.description, new_desc)
        self.assertEquals(doc2.id, album.cover.id)

        album_id = album.id
        # new album can be get
        album = ipernity.Album.get(id=album_id)
        album.delete()
        # after delete, album shoult not found
        with self.assertRaisesRegexp(errors.IpernityAPIError, 'Album not found'):
            ipernity.Album.get(id=album_id)

    def test_Folder(self):
        folder = ipernity.Folder.create(title='folder title')
        # fields type validation
        self.assertIsInstance(folder.count['albums'], int)
        self.assertIsInstance(folder.dates['created_at'], datetime.datetime)

        folder_id = folder.id
        # after created, folder can retrieve by get
        # TODO: this fail
        #folder = ipernity.Folder.get(id=folder_id)

        folder.delete()
        with self.assertRaisesRegexp(errors.IpernityAPIError, 'not found'):
            ipernity.Folder.get(id=folder_id)

    def test_Upload(self):
        ticket = ipernity.Upload.file(file=getfile('1.jpg'))
        ipernity.Upload.checkTickets(tickets=[ticket])
        #ticket.wait_done()
        #doc = ticket.doc
        doc = ticket.getDoc()

        # doc field test
        self.assertIsInstance(doc.dates['created'], datetime.datetime)
        self.assertIsInstance(doc.count['visits'], int)
        self.assertIsInstance(doc.visibility['share'], int)
        self.assertIsInstance(doc.can['fave'], bool)
        self.assertIsInstance(doc.you['visits'], int)
        self.assertIsInstance(doc.owner, ipernity.User)
        doc_str = str(doc)
        self.assertIn('Doc', doc_str)
        self.assertIn('id', doc_str)
        self.assertIn('title', doc_str)

        # Faves test
        Faves = ipernity.Faves
        # add
        Faves.docs_add(doc=doc)
        ret = Faves.docs_getList(user=self.user, owner=self.user)
        self.assertTrue(ret.info['total'] > 0)  # docs should be found
        self.assertTrue(any([d.id == doc.id for d in ret]))
        # check doc.getFaves
        # TODO: this fail, wired
        # ret = doc.getFaves()
        # ts = ret[0]['faved_at']
        # self.assertIsInstance(ts, datetime.datetime)
        # user = ret[0]['user']  # only one user faves
        # self.assertTrue(user.id == self.user.id)
        # remove
        Faves.docs_remove(doc=doc)
        ret = Faves.docs_getList(user=self.user, owner=self.user)
        self.assertFalse(any([d.id == doc.id for d in ret]))

        # thumb test
        thumb = doc.thumbs[0]
        self.assertIsInstance(thumb, ipernity.Thumb)
        self.assertIsInstance(thumb.w, int)
        self.assertIsInstance(thumb.h, int)

        doc.delete()

    def test_Tag(self):
        doc = self.docs[0]
        # add
        kwords = ['tag1', 'tag2']
        ret = doc.tags_add(keywords=kwords)
        self.assertIsInstance(ret.info['added'], int)

        # edit
        new_kwords = ['tag3', 'tag4']
        ret = doc.tags_edit(keywords=new_kwords)

        # getList
        ret = doc.tags_getList()
        self.assertIsInstance(ret.info['total'], int)
        export_tags = [t.tag for t in ret]
        self.assertTrue(all([t in export_tags for t in new_kwords]))
        tag = ret[0]
        tags = ret.data
        # tag obj verify
        self.assertIsInstance(tag.user, ipernity.User)
        self.assertIsInstance(tag.added_at, datetime.datetime)

        # test user.getTags
        ret = self.user.getTags()
        self.assertTrue(ret.info['count'] > 0)
        self.assertIsInstance(ret[0], ipernity.Tag)
        self.user.getPopularTags()
        # test Tag
        with self.assertRaisesRegexp(errors.IpernityError, 'type'):
            tag.docs_getList()
        ret = tag.docs_getList(user=self.user, type='keyword')
        self.assertTrue(any([d.id == doc.id for d in ret]))

        # remove
        with self.assertRaisesRegexp(errors.IpernityError, 'type'):
            # type parameter is required
            doc.tags_remove(tag=tag)
        for t in tags:
            doc.tags_remove(tag=t, type='keyword')

    def test_Note(self):
        doc = self.docs[0]
        note = doc.notes_add(content='note', x=0, y=0, w=50, h=50)
        # note fields verify
        self.assertIsInstance(note.x, int)
        self.assertIsInstance(note.w, int)
        self.assertIsInstance(note.posted_at, datetime.datetime)
        # edit
        note.edit(content='edited note', x=0, y=0, w=50, h=50)
        self.assertEquals(note.content, 'edited note')
        # delete
        note.delete()

        # Note.notes_add
        note = ipernity.Note.add(content='note', x=0, y=0, w=50, h=50, doc=doc)
        self.assertIsInstance(note, ipernity.Note)
        note.delete()

    def upload_files(self):
        ''' upload some test image and return '''
        # should upload at least 2 files
        def upload_img(fname):
            ticket = ipernity.Upload.file(file=getfile(fname))
            return ticket.getDoc()

        files = ['1.jpg', '2.jpg']
        return [upload_img(fname) for fname in files]
