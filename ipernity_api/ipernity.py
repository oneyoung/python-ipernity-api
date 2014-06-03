import datetime
import time
import re
from UserList import UserList
from .errors import IpernityError
from .reflection import call, static_call


class IpernityList(UserList):
    def __init__(self, data, info=None):
        UserList.__init__(self, data)
        self.info = info

    def __str__(self):
        return '%s:%s' % (str(self.info), str(self.data))

    def __repr__(self):
        return '%s:%s' % (repr(self.info), repr(self.data))


class IpernityObject(object):
    # convertors is a list of tuple ([attr1, attr2, ...], conv_func)
    __convertors__ = []
    # replace is a list consist of (oldname, newname, conv_func)
    __replace__ = []
    # __display__ fields to be shown in __str__, default only show id
    __display__ = []
    # attr name represent object's id in ipernity.com, e,g photo_id, user_id
    # if present, will add a filed that call 'id'
    __id__ = ''

    def __init__(self, **params):
        self._set_props(**params)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        raise IpernityError('Attr: Read-Only')

    def __repr__(self):
        cls = self.__class__
        clsname = cls.__name__
        fields = cls.__display__ or [cls.__id__]
        info = ' '.join(['%s:%s' % (attr, getattr(self, attr))
                         for attr in
                         filter(lambda a: hasattr(self, a), fields)])
        return '%s[%s]' % (clsname, info)

    def _set_props(self, **params):
        # implemnet of __convertors__
        for keys, func in self.__class__.__convertors__:
            for k in keys:
                try:
                    params[k] = func(params[k])
                except KeyError:
                    pass
        # implement of __replace__
        for old, new, func in self.__class__.__replace__:
            try:
                val = params.pop(old)
                params[new] = func(val)
            except KeyError:
                pass
        # implement __id__ mechanism
        idname = self.__class__.__id__
        if idname:
            idval = params.get('id') or params.get(idname)
            params['id'] = params[idname] = idval
        self.__dict__.update(params)


def _extract(name):
    ''' extract result with name from json response '''
    return lambda r: r[name]


def _none(resp):
    pass


def _str2bool(s):
    return bool(int(s))


def _dict_str2int(d, recurse=True):
    ''' convert string to int, traverse dict '''
    for k, v in d.items():
        if (isinstance(v, unicode) or isinstance(v, str)) and v.isdigit():
            d[k] = int(v)
        elif recurse:
            if isinstance(v, dict):
                d[k] = _dict_str2int(v)
            elif isinstance(v, list):
                d[k] = [_dict_str2int(l) for l in v]
    return d


def _dict_conv(conv_func):
    def convert(d):
        for k, v in d.items():
            d[k] = conv_func(v)
        return d

    return convert


def _ts2datetime(ts):
    regexp = r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d'
    if ts.isdigit():
        return datetime.datetime.fromtimestamp(int(ts))
    elif re.match(regexp, ts):
        try:
            return datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # timestamp might be '0000-00-00 00:00:00',
            # and will raise ValueError
            return None
    else:
        return ts or None


def _replaceid(kwargs, idname):
    ''' replace parameter 'id' with real id name 'idname' '''
    if idname not in kwargs and 'id' in kwargs:
        idval = kwargs.pop('id')
        kwargs[idname] = idval
    return kwargs


def _convert_iobj(kwargs, src, dst=None):
    ''' replace IpernityObject parameter with id

    params:
        kwargs: parameters dict to be handle
        src: var name to be convert
        dst: assign to new var name
    '''
    dst = dst or src + '_id'
    if dst not in kwargs and src in kwargs:
        iobj = kwargs.pop(src)
        if not isinstance(iobj, IpernityObject) or not hasattr(iobj, 'id'):
            raise ValueError('Invalid IpernityObject for %s' % src)
        kwargs[dst] = iobj.id
    return kwargs


def _dict_mapping(d, mapping):
    for k, func in mapping:
        if k in d:
            d[k] = func(d[k])
    return d


def _dict_mapping_func(mapping):
    def func(d):
        return _dict_mapping(d, mapping)
    return func


def _dict_list2str(kwargs, keys):
    for key in keys:
        if key in kwargs:
            val = kwargs[key]
            if isinstance(val, list):
                kwargs[key] = ','.join(val)
    return kwargs


# ### format result functions
def _resp2ilist(key, func_info, func_list, sec=''):
    ''' function generator for converting response to IpernityList

    parameters:
        name: the key of dict which point to the list
        func_info: func to convert info part
        func_list: func to convert list elem
        sec: section name, if not provided, will use: key + 's'
    '''
    def convertor(resp):
        sec_name = sec or key + 's'  # section name
        info = resp[sec_name]
        data = [func_list(e) for e in info.pop(key, [])]
        info = func_info(info)
        return IpernityList(data, info)
    return convertor


_format_result_albums = _resp2ilist('album', _dict_str2int,
                                    lambda d: Album(**d))
_format_result_docs = _resp2ilist('doc', _dict_str2int, lambda d: Doc(**d))
_format_result_faves = _resp2ilist('fave', _dict_str2int, lambda f: {
    'user': User(id=f.get('user_id'), username=f.get('username', '')),
    'faved_at': _ts2datetime(f.get('faved_at', 0)),
})
_format_result_groups = _resp2ilist('group', _dict_str2int,
                                    lambda g: Group(**g))
_format_result_network = _resp2ilist('user', _dict_str2int,
                                     lambda u: User(**u), sec='network')
_format_result_tags = _resp2ilist('tag', _dict_mapping_func([('count', int),
                                                             ('total', int),
                                                             ('dropped', int),
                                                             ('added', int)]),
                                  lambda t: Tag(**t))


def _format_result_visitors(resp):
    info = resp['visits']
    mapping = [
        ('visited_at', _ts2datetime),
        ('first_visit_at', _ts2datetime),
        ('visits', int),
    ]

    def conv_visit(visit):
        uid = visit.pop('user_id')
        uname = visit.pop('username')
        visit = _dict_mapping(visit, mapping)
        visit['user'] = User(id=uid, username=uname)
        return visit

    visits = [conv_visit(v) for v in info.pop('visit', [])]
    if 'anonymous' in info:
        info['anonymous'] = _dict_mapping(info['anonymous'], mapping)
    info = _dict_str2int(info)

    return IpernityList(visits, info)


class Test(IpernityObject):
    @static_call('test.echo')
    def echo(**kwargs):
        return kwargs, _extract('echo')

    @static_call('test.hello')
    def hello(**kwargs):
        return kwargs, _extract('hello')


class User(IpernityObject):
    __id__ = 'user_id'
    __display__ = ['id', 'username']
    __convertors__ = [
        (['is_pro', 'is_online', 'is_closed'], _str2bool),
        (['count'], _dict_conv(int)),
        (['dates'], _dict_conv(_ts2datetime)),
    ]

    @static_call('user.get')
    def get(**kwargs):
        kwargs = _replaceid(kwargs, User.__id__)
        return kwargs, lambda r: User(**r['user'])

    @static_call('account.getQuota')
    def getQuota(**kwargs):
        return kwargs, lambda r: Quota(**r['quota'])

    def getDocs(self, **kwargs):
        return Doc.getList(user=self, **kwargs)

    def getAlbums(self, **kwargs):
        return Album.getList(user=self, **kwargs)

    def getTags(self, type='keyword', **kwargs):
        return Tag.user_getList(user=self, type=type, **kwargs)

    def getPopularTags(self, type='keyword', **kwargs):
        return Tag.user_getPopular(user=self, type=type, **kwargs)

    def getNetworks(self, **kwargs):
        return Network.getList(user=self, **kwargs)

    def getGroups(self, **kwargs):
        return Group.getList(user=self, **kwargs)


class Quota(IpernityObject):
    __convertors__ = [
        (['is_pro'], _str2bool),
        (['upload'], _dict_str2int),
    ]


class Auth(IpernityObject):
    @static_call('auth.checkToken')
    def get(**kwargs):
        return kwargs, lambda r: Auth(**r['auth'])


class Album(IpernityObject):
    __id__ = 'album_id'
    __display__ = ['id', 'title']
    __convertors__ = [
        (['count'], _dict_conv(int)),
        (['dates'], _dict_conv(_ts2datetime)),
        (['cover'], lambda c: Doc(**c) if isinstance(c, dict) else c),
    ]

    @static_call('album.create')
    def create(**kwargs):
        kwargs = _convert_iobj(kwargs, 'cover')
        return kwargs, lambda r: Album(**r['album'])

    @static_call('album.get')
    def get(**kwargs):
        kwargs = _replaceid(kwargs, Album.__id__)
        return kwargs, lambda r: Album(**r['album'])

    @static_call('album.getList')
    def getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _resp2ilist('album', _dict_str2int,
                                   lambda d: Album(**d))

    @call('album.delete')
    def delete(self, **kwargs):
        return kwargs, _none

    @call('album.edit')
    def edit(self, **kwargs):
        kwargs = _convert_iobj(kwargs, 'cover')
        # result should update to self
        return kwargs, lambda r: self._set_props(**r['album'])

    @call('album.getFaves')
    def getFaves(self, **kwargs):
        return kwargs, _format_result_faves

    @call('album.getVisitors')
    def getVisitors(self, **kwargs):
        return kwargs, _format_result_visitors

    @call('album.docs.add')
    def docs_add(self, **kwargs):
        def format_result(resp):
            info = resp['album']
            info.pop('album_id', None)
            info = _dict_str2int(info, False)
            mapping = [
                ('added', _str2bool),
                ('error', _str2bool),
            ]
            docs = [_dict_mapping(d, mapping) for d in info.pop('doc', [])]
            return IpernityList(docs, info=info)

        try:
            if 'doc' in kwargs:
                doc_id = kwargs.pop('doc').id
            elif 'docs' in kwargs:
                doc_id = ','.join([doc.id if isinstance(doc, Doc) else doc
                                  for doc in kwargs.pop('docs')])
            else:
                doc_id = kwargs.pop('doc_id')
        except:
            raise IpernityError('No or Invalid doc provided')
        kwargs['doc_id'] = doc_id

        return kwargs, format_result


class Folder(IpernityObject):
    __id__ = 'folder_id'
    __display__ = ['id', 'title']
    __convertors__ = [
        (['count'], _dict_conv(int)),
        (['dates'], _dict_conv(_ts2datetime)),
    ]

    @static_call('folder.create')
    def create(**kwargs):
        return kwargs, lambda r: Folder(**r['folder'])

    @static_call('folder.get')
    def get(**kwargs):
        kwargs = _replaceid(kwargs, Folder.__id__)
        return kwargs, lambda r: Folder(**r['folder'])

    @call('folder.delete')
    def delete(self, **kwargs):
        return kwargs, _none


class Upload(IpernityObject):
    @static_call('upload.file')
    def file(**kwargs):
        return kwargs, lambda r: Ticket(id=r['ticket'])

    @static_call('upload.checkTickets')
    def checkTickets(**kwargs):
        if 'tickets' not in kwargs:
            raise IpernityError('No tickets provided')
        tickets = kwargs.pop('tickets')
        kwargs['tickets'] = ','.join([t.id if isinstance(t, Ticket) else t
                                      for t in tickets])
        return kwargs, _resp2ilist('ticket', _dict_str2int,
                                   lambda d: Ticket(**d))


class Ticket(IpernityObject):
    __convertors__ = [
        (['done', 'invalid'], _str2bool),
        (['eta'], int),
    ]

    __replace__ = [
        ('doc_id', 'doc', lambda id: Doc(id=id)),
    ]

    def refresh(self):
        new = Upload.checkTickets(tickets=[self])[0]
        meta = {}
        for attr in ['done', 'invalid', 'doc_id', 'eta']:
            if hasattr(new, attr):
                meta[attr] = getattr(new, attr)
        if hasattr(new, 'doc'):
            meta['doc_id'] = new.doc.id
        return self._set_props(**meta)

    def wait_done(self, timeout=100):
        ''' wait upload done

        parameters:
            timeout: optional timeout to specified max wait time, default 100s
        '''
        if getattr(self, 'invalid', False):
            raise IpernityError('Ticket: %s Invalid' % self)

        left = timeout
        while not getattr(self, 'done', False) and left > 0:
            # wait upload complete
            # first time, Ticket only init with id, not 'eta' field provide
            eta = getattr(self, 'eta', 0)
            left -= eta
            time.sleep(eta)
            self.refresh()
        if not getattr(self, 'done', False):
            raise IpernityError('Timeout for wait done after %ss' % timeout)

    def getDoc(self):
        self.wait_done()
        doc_id = self.doc.id
        return Doc.get(id=doc_id)


def _conv_you(you):
    mapping = [
        ('isfave', _str2bool),
        ('visits', int),
        ('last_visit', _ts2datetime),
        # you in group.get
        ('joined_at', _ts2datetime),
        ('visited_at', _ts2datetime),
        ('isadmin', _str2bool),
        ('ismoderator', _str2bool),
        ('ismember', _str2bool),
        ('docs', int),
    ]
    return _dict_mapping(you, mapping)


class File(IpernityObject):
    __display__ = ['label', 'url']
    __convertors__ = [
        (['w', 'h', 'lehgth', 'bytes'], int),
    ]


class Thumb(File):
    pass


class Media(File):
    pass


class Original(File):
    pass


class Player(File):
    pass


class Doc(IpernityObject):
    __id__ = 'doc_id'
    __display__ = ['id', 'title']
    __convertors__ = [
        (['w', 'h', 'lehgth', 'bytes', 'index'], int),
        (['dates'], _dict_conv(_ts2datetime)),
        (['count', 'visibility', 'permissions'], _dict_conv(int)),
        (['can'], _dict_conv(_str2bool)),
        (['you'], _conv_you),
        (['owner'], lambda r: User(**r)),
        (['thumbs'], lambda tbs: [Thumb(**tb) for tb in tbs['thumb']]),
        (['medias'], lambda mds: [Media(**md) for md in mds['media']]),
        (['original'], lambda o: Original(**o)),
    ]

    @static_call('doc.getList')
    def getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user', 'user_id')
        return kwargs, _format_result_docs

    @static_call('doc.checkMD5')
    def checkMD5(**kwargs):
        # This method will work someday... (ask us about if you need it)
        def format_result(resp):
            def conv_doc(d):
                found = _str2bool(int(d['found']))
                d['found'] = found
                if found:
                    doc = Doc(id=d.pop('doc_id'))
                    d['doc'] = doc
                return d

            info = resp['docs']
            docs = [conv_doc(d) for d in info.pop('doc', [])]
            info = _dict_str2int(info)
            return IpernityList(docs, info)

        if 'md5s' in kwargs:
            md5s = ','.join(kwargs.pop('md5s', []))
            kwargs['md5'] = md5s
        return kwargs, format_result

    @static_call('doc.get')
    def get(**kwargs):
        kwargs = _replaceid(kwargs, Doc.__id__)
        return kwargs, lambda r: Doc(**r['doc'])

    @call('doc.getContainers')
    def getContainers(self, **kwargs):
        def format_result(resp):
            return {
                'albums': _format_result_albums(resp),
                'groups': _format_result_groups(resp),
            }

        return kwargs, format_result

    @call('doc.getContext')
    def getContext(self, **kwargs):
        def format_result(resp):
            return {
                'doc': Doc(**resp['doc']),
                'prev': _resp2ilist('doc', _dict_str2int,
                                    lambda d: Doc(**d), sec='prev')(resp),
                'next': _resp2ilist('doc', _dict_str2int,
                                    lambda d: Doc(**d), sec='next')(resp),
            }
        return kwargs, format_result

    @call('doc.getFaves')
    def getFaves(self, **kwargs):
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, _format_result_faves

    @call('doc.getMedias')
    def getMedias(self, **kwargs):
        def format_result(resp):
            return {
                'thumbs': [Thumb(**t)
                           for t in resp['thumbs'].pop('thumb', [])]
                if 'thumbs' in resp else [],
                'medias': [Media(**m)
                           for m in resp['medias'].pop('media', [])]
                if 'medias' in resp else [],
                'players': [Player(**p)
                            for p in resp['players'].pop('player', [])]
                if 'players'in resp else [],
                'original': Original(**resp['original'])
                if 'original' in resp else None
            }
        return kwargs, format_result

    @call('doc.getPerms')
    def getPerms(self, **kwargs):
        def format_result(resp):
            return {
                'visibility': _dict_str2int(resp['visibility']),
                'permissions': _dict_str2int(resp['permissions']),
                'can': _dict_conv(_str2bool)(resp['can']),
            }
        return kwargs, format_result

    @call('doc.delete')
    def delete(self, **kwargs):
        return kwargs, _none

    # comments
    def comments_add(self, **kwargs):
        return Comment.add(doc=self, **kwargs)

    def comments_getList(self, **kwargs):
        return Comment.getList(doc=self, **kwargs)

    # notes
    @call('doc.notes.add')
    def notes_add(self, **kwargs):
        kwargs = _convert_iobj(kwargs, 'member')
        return kwargs, lambda r: Note(**r['note'])

    # tags handling
    @call('doc.tags.add')
    def tags_add(self, **kwargs):
        kwargs = _dict_list2str(kwargs, ['keywords', 'members'])
        return kwargs, _format_result_tags

    @call('doc.tags.edit')
    def tags_edit(self, **kwargs):
        kwargs = _dict_list2str(kwargs, ['keywords', 'members'])
        return kwargs, _format_result_tags

    @call('doc.tags.getList')
    def tags_getList(self, **kwargs):
        return kwargs, _format_result_tags

    @call('doc.tags.remove')
    def tags_remove(self, **kwargs):
        if 'tag' in kwargs:
            tag = kwargs.pop('tag')
            if not isinstance(tag, Tag):
                raise IpernityError('Invalid tag')
            kwargs['id'] = tag.id
        return kwargs, _none


class Faves(IpernityObject):
    @static_call('faves.albums.add')
    def albums_add(**kwargs):
        kwargs = _convert_iobj(kwargs, 'album')
        return kwargs, _none

    @static_call('faves.albums.remove')
    def albums_remove(**kwargs):
        kwargs = _convert_iobj(kwargs, 'album')
        return kwargs, _none

    @static_call('faves.albums.getList')
    def albums_getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        kwargs = _convert_iobj(kwargs, 'owner')
        return kwargs, _format_result_albums

    @static_call('faves.docs.add')
    def docs_add(**kwargs):
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, _none

    @static_call('faves.docs.remove')
    def docs_remove(**kwargs):
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, _none

    @static_call('faves.docs.getList')
    def docs_getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        kwargs = _convert_iobj(kwargs, 'owner')
        return kwargs, _format_result_docs


class Tag(IpernityObject):
    __id__ = 'id'
    __display__ = ['id', 'tag']
    __convertors__ = [
        (['added_at'], _ts2datetime),
    ]
    __replace__ = [
        ('user_id', 'user', lambda uid: User(id=uid)),
    ]

    @static_call('tags.user.getList')
    def user_getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _format_result_tags

    @static_call('tags.user.getPopular')
    def user_getPopular(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _format_result_tags

    @call('tags.docs.getList')
    def docs_getList(self, **kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _format_result_docs


class Note(IpernityObject):
    __id__ = 'note_id'
    __convertors__ = [
        (['x', 'y', 'w', 'h'], int),
        (['posted_at'], _ts2datetime),
    ]

    @static_call('doc.notes.add')
    def add(**kwargs):
        kwargs = _convert_iobj(kwargs, 'member')
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, lambda r: Note(**r['note'])

    @call('doc.notes.edit')
    def edit(self, **kwargs):
        return kwargs, lambda r: self._set_props(**r['note'])

    @call('doc.notes.delete')
    def delete(self, **kwargs):
        return kwargs, _none


class Comment(IpernityObject):
    __id__ = 'comment_id'
    __convertors__ = [
        (['posted_at'], _ts2datetime),
        (['candelete', 'canedit', 'canreply'], _str2bool),
    ]
    __replace__ = [
        ('parent_id', 'parent', lambda cid: Comment(id=cid)),
        ('user_id', 'user', lambda uid: User(id=uid)),
    ]

    @static_call('doc.comments.add')
    def add(**kwargs):
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, lambda r: Comment(**r['comment'])

    @call('doc.comments.delete')
    def delete(self, **kwargs):
        return kwargs, _none

    @call('doc.comments.edit')
    def edit(self, **kwargs):
        return kwargs, lambda r: self._set_props(**r['comment'])

    @call('doc.comments.get')
    def get(self, **kwargs):
        return kwargs, lambda r: Comment(**r['comment'])

    @call('doc.comments.reply')
    def reply(self, **kwargs):
        return kwargs, lambda r: Comment(**r['comment'])

    @static_call('doc.comments.getList')
    def getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'doc')
        return kwargs, _resp2ilist('comment', _dict_str2int,
                                   lambda c: Comment(**c))


class Network(IpernityObject):
    @static_call('network.autocomplete')
    def autocomplete(**kwargs):
        return kwargs, _format_result_network

    @static_call('network.getList')
    def getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _format_result_network

    @static_call('network.docs.getRecent')
    def docs_getRecent(**kwargs):
        return kwargs, _format_result_docs


class Group(IpernityObject):
    __id__ = 'group_id'
    __display__ = ['id', 'title']
    __convertors__ = [
        (['can', 'visibility'], _dict_conv(_str2bool)),
        (['quota', 'count'], _dict_str2int),
        (['dates'], _dict_conv(_ts2datetime)),
        (['you'], _conv_you),
    ]

    @static_call('group.getList')
    def getList(**kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, _format_result_groups

    @static_call('group.search')
    def search(**kwargs):
        return kwargs, _format_result_groups

    @call('group.get')
    def get(self, **kwargs):
        return kwargs, lambda r: Group(**r['group'])

    @call('group.get')
    def update(self, **kwargs):
        return kwargs, lambda r: self._set_props(**r['group'])

    def _docs_add_remove(self, **kwargs):
        def format_result(resp):
            def format_doc(doc):
                doc['doc'] = Doc(id=doc.pop('doc_id'))
                for k in ['added', 'pending', 'error', 'removed']:
                    if k in doc:
                        doc[k] = _str2bool(doc[k])
                return doc

            info = resp['group']
            info.pop('group_id', None)
            docs = [format_doc(doc) for doc in info.pop('doc', [])]
            info = _dict_str2int(info)
            return IpernityList(docs, info)

        if 'docs' in kwargs:
            docs = ','.join([d.id if isinstance(d, Doc) else d
                             for d in kwargs.pop('docs')])
            kwargs['doc_id'] = docs
        return kwargs, format_result

    @call('group.docs.add')
    def docs_add(self, **kwargs):
        return self._docs_add_remove(**kwargs)

    @call('group.docs.remove')
    def docs_remove(self, **kwargs):
        return self._docs_add_remove(**kwargs)

    @call('group.docs.getList')
    def docs_getList(self, **kwargs):
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, lambda r: _format_result_docs(r['group'])

    @call('group.docs.getContext')
    def docs_getContext(self, **kwargs):
        def format_result(resp):
            info = resp
            return {
                'doc': Doc(**info['doc']),
                'prev': _resp2ilist('doc', _dict_str2int,
                                    lambda d: Doc(**d), sec='prev')(info),
                'next': _resp2ilist('doc', _dict_str2int,
                                    lambda d: Doc(**d), sec='next')(info),
                'total': int(info['group']['total']),
            }
        kwargs = _convert_iobj(kwargs, 'doc')
        kwargs = _convert_iobj(kwargs, 'user')
        return kwargs, format_result


class Explore(IpernityObject):
    @static_call('explore.docs.getPopular')
    def docs_getPopular(**kwargs):
        return kwargs, _format_result_docs

    @static_call('explore.docs.getRecent')
    def docs_getRecent(**kwargs):
        return kwargs, _format_result_docs

    @static_call('explore.docs.homepage')
    def docs_homepage(**kwargs):
        return kwargs, _format_result_docs

    @static_call('explore.groups.getRandom')
    def groups_getRandom(**kwargs):
        return kwargs, _format_result_groups
