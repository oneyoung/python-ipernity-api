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
    # attr name that represent object's id in ipernity.com, e,g photo_id, user_id
    # if present, will add a filed that call 'id'
    __id__ = ''

    def __init__(self, **params):
        self._set_props(**params)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        raise IpernityError('Attr: Read-Only')

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


def _dict_str2int(d):
    ''' convert string to int, traverse dict '''
    for k, v in d.items():
        if (isinstance(v, unicode) or isinstance(v, str)) and v.isdigit():
            d[k] = int(v)
        elif isinstance(v, dict):
            d[k] = _dict_str2int(v)
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
        # timestamp might be '0000-00-00 00:00:00', and will raise ValueError
            return None
    else:
        return ts or None


def _replaceid(kwargs, idname):
    ''' replace parameter 'id' with real id name 'idname' '''
    if idname not in kwargs and 'id' in kwargs:
        idval = kwargs.pop('id')
        kwargs[idname] = idval
    return kwargs


class Test(IpernityObject):
    @static_call('test.echo')
    def echo(**kwargs):
        return kwargs, _extract('echo')

    @static_call('test.hello')
    def hello(**kwargs):
        return kwargs, _extract('hello')


class User(IpernityObject):
    __id__ = 'user_id'
    __convertors__ = [
        (['is_pro', 'is_online', 'is_closed'], bool),
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


class Quota(IpernityObject):
    __convertors__ = [
        (['is_pro'], bool),
        (['upload'], _dict_str2int),
    ]


class Auth(IpernityObject):
    @static_call('auth.checkToken')
    def get(**kwargs):
        return kwargs, lambda r: Auth(**r['auth'])


class Album(IpernityObject):
    __id__ = 'album_id'
    __convertors__ = [
        (['count'], _dict_conv(int)),
        (['dates'], _dict_conv(_ts2datetime)),
    ]

    @static_call('album.create')
    def create(**kwargs):
        return kwargs, lambda r: Album(**r['album'])

    @static_call('album.get', force_auth=True)
    def get(**kwargs):
        kwargs = _replaceid(kwargs, Album.__id__)
        return kwargs, lambda r: Album(**r['album'])

    @call('album.delete')
    def delete(self, **kwargs):
        return kwargs, _none

    @call('album.edit')
    def edit(self, **kwargs):
        # TODO: add cover_id here, update from doc objects
        # result should update to self
        return kwargs, lambda r: self._set_props(**r['album'])


class Folder(IpernityObject):
    __id__ = 'folder_id'
    __convertors__ = [
        (['count'], _dict_conv(int)),
        (['dates'], _dict_conv(_ts2datetime)),
    ]

    @static_call('folder.create')
    def create(**kwargs):
        return kwargs, lambda r: Folder(**r['folder'])

    @static_call('folder.get', force_auth=True)
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
        def format_result(resp):
            info = resp['tickets']
            tickets = info.pop('ticket')
            return IpernityList([Ticket(**t) for t in tickets], info=info)

        if 'tickets' not in kwargs:
            raise IpernityError('No tickets provided')
        tickets = kwargs.pop('tickets')
        kwargs['tickets'] = ','.join([t.id if isinstance(t, Ticket) else t
                                      for t in tickets])
        return kwargs, format_result


class Ticket(IpernityObject):
    __convertors__ = [
        (['done', 'invalid'], bool),
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
        while not getattr(self, 'done', False) and left > 0:  # wait upload complete
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
        ('isfave', bool),
        ('visits', int),
        ('last_visit', _ts2datetime),
    ]
    for name, func in mapping:
        if name in you:
            you[name] = func(you[name])
    return you


class File(IpernityObject):
    __convertors__ = [
        (['w', 'h', 'lehgth', 'bytes'], int),
    ]
    # media type, could be thumb/media/original
    type = ''


class Thumb(File):
    type = 'thumb'


class Media(File):
    type = 'media'


class Original(File):
    type = 'original'


class Doc(IpernityObject):
    __id__ = 'doc_id'
    __convertors__ = [
        (['dates'], _dict_conv(_ts2datetime)),
        (['count', 'visibility', 'permissions'], _dict_conv(int)),
        (['can'], _dict_conv(bool)),
        (['you'], _conv_you),
        (['owner'], lambda r: User(**r)),
        (['thumbs'], lambda tbs: [Thumb(**tb) for tb in tbs['thumb']]),
        (['medias'], lambda mds: [Media(**md) for md in mds['media']]),
        (['original'], lambda o: Original(**o)),
    ]

    @static_call('doc.get')
    def get(**kwargs):
        kwargs = _replaceid(kwargs, Doc.__id__)
        return kwargs, lambda r: Doc(**r['doc'])

    @call('doc.delete')
    def delete(self, **kwargs):
        return kwargs, _none
