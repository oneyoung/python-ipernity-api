import os
import datetime
import ipernity_api as ipernity
from unittest import TestCase
from ipernity_api import errors
from . import utils


def getfile(fname):
    return os.path.join(os.path.dirname(__file__), 'files', fname)


class IpernityTest(TestCase):
    # TODO: has no way to test Post

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

        # add doc
        ret = album.docs_add(doc=doc1)
        # check result
        self.assertEqual(ret.info['total'], 1)
        self.assertIsInstance(ret[0]['added'], bool)
        # doc.getContainers
        ret = doc1.getContainers()
        self.assertTrue(any([a.id == album.id for a in ret['albums']]))
        # add docs
        album.docs_add(docs=[doc1, doc2])

        # docs_setList
        ret = album.docs_setList(docs=[doc2, doc1], cover=doc2)
        self.assertEquals(ret.info['cover'].id, doc2.id)
        self.assertIsInstance(ret.info['total'], int)
        self.assertTrue(any([doc1.id == d['doc'].id for d in ret]))

        # docs_getContext
        ret = album.docs_getContext(doc=doc1)
        self.assertEquals(ret['doc'].id, album.id)
        self.assertTrue(all([isinstance(d, ipernity.Doc)
                             for d in ret['prev']]))
        self.assertTrue(all([isinstance(d, ipernity.Doc)
                             for d in ret['next']]))

        # getList test
        ret = ipernity.Album.getList(user=self.user)
        self.assertTrue(ret.info['total'] > 0)
        self.assertTrue(any([a.id == album.id for a in ret]))

        # orderList
        albums = ret.data
        albums.reverse()
        ipernity.Album.orderList(albums=albums)

        # setPerms
        album.setPerms(perm_comment=5)

        # docs_getList
        ret = album.docs_getList()
        self.assertTrue(any([d.id == doc1.id for d in ret]))

        # Faves Test for Album
        Faves = ipernity.Faves
        ret = album.getFaves()
        self.assertEqual(ret.info['count'], 0)
        # Faves add and getList
        Faves.albums_add(album=album)  # add by Faves
        # verifiy Faves list
        ret = Faves.albums_getList(user=self.user, owner=self.user)
        self.assertTrue(ret.info['total'] > 0)
        self.assertTrue(any([a.id == album.id for a in ret]))
        # album.getFaves
        # TODO: this fail, wired
        # ret = album.getFaves()
        # ts = ret[0]['faved_at']
        # self.assertIsInstance(ts, datetime.datetime)
        # user = ret[0]['user']  # only one user faves
        # self.assertTrue(user.id == self.user.id)
        # remove it
        Faves.albums_remove(album=album)
        # verifiy Faves list
        ret = Faves.albums_getList(user=self.user, owner=self.user)
        # should not found
        self.assertFalse(any([a.id == album.id for a in ret.data]))

        # getVisitors
        ret = album.getVisitors()
        self.assertIsInstance(ret.info['total'], int)

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

        # docs_remove
        ret = album.docs_remove(docs=[doc1])
        self.assertIsInstance(ret.info['total'], int)
        self.assertIsInstance(ret[0]['removed'], bool)
        self.assertTrue(any([doc1.id == d['doc'].id for d in ret]))

        # delete album
        # it's wired, once albums has not docs, album delete would not found
        album.delete()
        # after delete, album shoult not found
        with self.assertRaisesRegexp(errors.IpernityAPIError,
                                     'Album not found'):
            ipernity.Album.get(id=album_id)

    def test_Folder(self):
        folder = ipernity.Folder.create(title='folder title')
        # fields type validation
        self.assertIsInstance(folder.count['albums'], int)
        self.assertIsInstance(folder.dates['created_at'], datetime.datetime)

        # albums_add
        a1 = ipernity.Album.create(title='album1')
        a1.docs_add(docs=self.docs)
        ret = folder.albums_add(albums=[a1])
        self.assertTrue(ret.info['total'] > 0)
        self.assertIsInstance(ret[0]['album'], ipernity.Album)
        self.assertIsInstance(ret[0]['added'], bool)

        # albums_getList
        ret = folder.albums_getList()
        self.assertTrue(any([a.id == a1.id for a in ret]))

        # edit
        folder.edit(title='new title', description='new desc')
        self.assertEquals(folder.title, 'new title')
        self.assertEquals(folder.description, 'new desc')

        # getList, userd by user.getFolders
        ret = self.user.getFolders(empty=True)
        self.assertTrue(ret.info['total'] > 0)
        self.assertTrue(all([isinstance(f, ipernity.Folder)
                             for f in ret]))

        # orderList
        ipernity.Folder.orderList(folders=[folder])

        folder_id = folder.id
        # after created, folder can retrieve by get
        folder = ipernity.Folder.get(id=folder_id)

        # Folder.albums_remove
        folder.albums_remove(albums=[a1])

        folder.delete()
        with self.assertRaisesRegexp(errors.IpernityAPIError, 'not found'):
            ipernity.Folder.get(id=folder_id)

        a1.delete()

    def test_Upload(self):
        ticket = ipernity.Upload.file(file=getfile('1.jpg'))
        ipernity.Upload.checkTickets(tickets=[ticket])
        # ticket.wait_done()
        # doc = ticket.doc
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

    def test_Doc(self):
        # This method will work someday... (ask us about if you need it)
        ipernity.Doc.checkMD5(md5s=['1cfe2ec123ac9eb7b6bdb5191c3efd40'])

        # doc.getContext
        doc = self.docs[1]
        ret = doc.getContext()
        self.assertEquals(ret['doc'].id, doc.id)
        for d in ret['prev']:
            self.assertIsInstance(d, ipernity.Doc)
            self.assertIsInstance(d['index'], int)
        self.assertTrue(all([isinstance(d, ipernity.Doc)
                             for d in ret['next']]))

        # doc.getMedias
        ret = doc.getMedias()
        if ret['thumbs']:
            self.assertTrue(all([isinstance(t, ipernity.Thumb)
                                 for t in ret['thumbs']]))

        # doc.getPerms
        ret = doc.getPerms()
        self.assertIsInstance(ret['visibility']['ispublic'], int)
        self.assertIsInstance(ret['permissions']['comment'], int)
        self.assertIsInstance(ret['can']['fave'], bool)

        # doc.setPerms
        doc.setPerms(perm_tagme=1)

        # doc.getVisitor
        doc.getVisitors()

        # doc.setLisence
        doc.setLicense(license=11)

        # doc.setGeo
        doc.setGeo(lng=43, lat=78.99)

        # doc.set
        doc.set(title='new title', description='new desc')
        self.assertEquals(doc.title, 'new title')
        self.assertEquals(doc.description, 'new desc')

        # doc.search
        ret = ipernity.Doc.search(user=self.user, tags=[])
        self.assertTrue(all([isinstance(d, ipernity.Doc) for d in ret]))
        ret = ipernity.Doc.search(user=self.user,
                                  created_max=datetime.datetime.now())
        self.assertTrue(all([isinstance(d, ipernity.Doc) for d in ret]))

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
        ret = tag.docs_getList(user=self.user, type='keyword')
        self.assertTrue(any([d.id == doc.id for d in ret]))

        # remove
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

    def test_Comment(self):
        doc = self.docs[0]
        c1 = doc.comments_add(content='content1')
        c2 = doc.comments_add(content='content2')

        # getList
        comms = doc.comments_getList()
        self.assertTrue(comms.info['count'] >= 2)
        self.assertTrue(any([c1.id == c.id for c in comms]))
        self.assertTrue(any([c2.id == c.id for c in comms]))

        # edit
        c1.edit(content='new')
        self.assertEquals(c1.content, 'new')

        # reply
        r = c1.reply(content='reply')
        # get
        g = r.get()
        # fields checking
        self.assertIsInstance(g.posted_at, datetime.datetime)
        self.assertIsInstance(g.user, ipernity.User)
        self.assertIsInstance(g.parent, ipernity.Comment)
        self.assertIsInstance(g.canedit, bool)
        self.assertIsInstance(g.canreply, bool)

        c1.delete()
        c2.delete()

    def test_Network(self):
        # Note: in order to have a full test, need to add somebody manually in
        # network on ipernity.com
        user = self.user
        networks = user.getNetworks()
        self.assertIsInstance(networks.info['count'], int)
        self.assertTrue(all([isinstance(u, ipernity.User) for u in networks]))
        # auto complete
        if len(networks):
            u = networks[0]
            ret = ipernity.Network.autocomplete(query=u.username)
            self.assertIsInstance(ret.info['count'], int)
            self.assertTrue(all([isinstance(u0, ipernity.User) for u0 in ret]))
        else:
            raise utils.TestCaseError('tested account has no networks, \
                                      need manually add in ipernity.com')
        # docs_getRecent
        docs = ipernity.Network.docs_getRecent()
        self.assertIsInstance(docs.info['count'], int)
        self.assertTrue(all([isinstance(doc, ipernity.Doc) for doc in docs]))

    def test_Group(self):
        # Note: need to manually add Group in ipernity.com
        user = self.user
        # getList
        groups = user.getGroups()
        self.assertIsInstance(groups.info['total'], int)
        if len(groups):
            group = groups[0]
            # fetch detail
            group.update()
            # field validation
            self.assertIsInstance(group.can['add_doc'], bool)
            self.assertIsInstance(group.visibility['ispublic'], bool)
            self.assertIsInstance(group.quota['max'], int)
            self.assertIsInstance(group.count['docs'], int)
            self.assertIsInstance(group.dates['created_at'], datetime.datetime)
            self.assertIsInstance(group.you['isadmin'], bool)
            self.assertIsInstance(group.you['joined_at'], datetime.datetime)
            self.assertIsInstance(group.you['docs'], int)

            # search test
            ret = ipernity.Group.search(text=group.title)
            self.assertTrue(all([isinstance(g, ipernity.Group) for g in ret]))

            # docs_add
            docs = self.docs[:2]
            ret = group.docs_add(docs=docs)
            self.assertTrue(ret.info['total'] > 0)
            self.assertTrue(any([docs[0].id == r['doc'].id for r in ret]))
            # doc.getContainers
            ret = docs[0].getContainers()
            self.assertTrue(any([g.id == group.id for g in ret['groups']]))
            # docs_getList
            ret = group.docs_getList(user=self.user)
            self.assertTrue(ret.info['total'] > 0)
            self.assertTrue(any([docs[0].id == d.id for d in ret]))
            # docs_getContext
            ret = group.docs_getContext(doc=docs[1])
            self.assertTrue(ret['total'] > 0)
            self.assertEquals(ret['doc'].id, docs[1].id)
            all_docs = ret['prev'] + ret['next']
            self.assertTrue(any([docs[0].id == d.id for d in all_docs]))
            # docs_remove
            ret = group.docs_remove(docs=docs)
        else:
            raise utils.TestCaseError('tested account has no groups, \
                                      need manually add in ipernity.com')

    def test_Explore(self):
        docs = ipernity.Explore.docs_getPopular()
        self.assertIsInstance(docs.info['total'], int)
        self.assertTrue(all([isinstance(doc, ipernity.Doc) for doc in docs]))

        docs = ipernity.Explore.docs_getRecent()
        self.assertIsInstance(docs.info['count'], int)
        self.assertTrue(all([isinstance(doc, ipernity.Doc) for doc in docs]))

        docs = ipernity.Explore.docs_homepage()
        self.assertTrue(all([isinstance(doc, ipernity.Doc) for doc in docs]))

        groups = ipernity.Explore.groups_getRandom()
        self.assertTrue(all([isinstance(g, ipernity.Group) for g in groups]))
