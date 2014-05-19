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
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        raise IpernityError('Attr: Read-Only')

    def _set_props(self, **params):
        self.__dict__.update(params)


def extract(name):
    ''' extract result with name from json response '''
    return lambda r: r[name]


class Test(IpernityObject):
    @static_call('test.echo')
    def echo(**kwargs):
        return kwargs, extract('echo')

    @static_call('test.hello')
    def hello(**kwargs):
        return kwargs, extract('hello')
