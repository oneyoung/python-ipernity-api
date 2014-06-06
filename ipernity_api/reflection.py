from functools import wraps, partial
from .methods import __methods__
from .errors import IpernityError
from .rest import call_api


def _required_params(info):
    params = info.get('parameters', [])
    requires = [p['name'] for p in
                filter(lambda p: bool(p.get('required', 0)), params)]
    # api_key would be handled in rest
    try:
        requires.remove('api_key')
    except ValueError:
        pass
    return requires


def call(api_method):
    ''' decorator to wrapper api method call for instance method

    Parameters:
        api_method: Ipernity method name to be called.
            we can't get the album, and always return 'Album not found')

    Note:
    * requirement for function:
        each function must return a tuple with (params, format_result), where
        "params" is a dict consist of parameters to ipernity api method.
        "format_result" is a function to decode json resonpse.
    * return value of decorated function:
        api json resonpse will be decoded by "format_result" function
        and return to caller.
    '''
    # use two level decorator here:
    # level 1: "call" to accept decorator paramter 'api_method'
    # level 2: "decorator" is the real decorator to accept function, this
    # decorator will finally return the wrapper functon "wrapper".
    def decorator(func):
        try:
            info = __methods__[api_method]
        except KeyError:
            raise IpernityError('Method %s not found' % api_method)
        requires = _required_params(info)
        auth_info = info['authentication']
        # partial object for this api call
        request = partial(call_api, api_method,
                          authed=auth_info['token'],
                          http_post=auth_info['post'],
                          signed=auth_info['sign'])

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            params, format_result = func(self, *args, **kwargs)
            # IpernityObject.__id__ handling
            idname = getattr(self.__class__, '__id__', None)
            if idname and idname not in params:
                params[idname] = self.id
            # required parameters checking
            if not all([p in params for p in requires]):
                raise IpernityError('parameters missing, required: %s'
                                    % ', '.join(requires))
            resp = request(**params)
            return format_result(resp)
        wrapper.ipernity_method = api_method
        wrapper.static = False
        return wrapper

    return decorator


class StaticCaller(staticmethod):
    def __init__(self, func):
        staticmethod.__init__(self, func)
        self.__dict__ = func.__dict__
        self.inner_func = func


def static_call(api_method):
    ''' call decorator for static method

    The same as 'call' decorator, except it design for class static method
    '''

    def decorator(func):
        try:
            info = __methods__[api_method]
        except KeyError:
            raise IpernityError('Method %s not found' % api_method)
        requires = _required_params(info)
        auth_info = info['authentication']
        # partial object for this api call
        request = partial(call_api, api_method,
                          authed=auth_info['token'],
                          http_post=auth_info['post'],
                          signed=auth_info['sign'])

        @wraps(func)
        def wrapper(*args, **kwargs):
            params, format_result = func(*args, **kwargs)
            # required parameters checking
            if not all([p in params for p in requires]):
                raise IpernityError('parameters missing, required: %s'
                                    % ','.join(requires))
            resp = request(**params)
            return format_result(resp)
        wrapper.ipernity_method = api_method
        wrapper.static = True
        return StaticCaller(wrapper)

    return decorator


def method_doc(method, ignore_params=[]):
    doc = '''
    API: %(method)s
    Description: %(desc)s
    Auth: %(auth)s
    Permission: %(perms)s
    %(params)s
    '''
    info = __methods__[method]
    desc = info['title']
    # resp = info['response']
    auth = 'Required' if info['authentication']['token'] else 'No Need'
    perms = ','.join(['%s:%s' % (k, v)
                      for k, v in info['permissions'].iteritems()]
                     if info['permissions'] else [])
    params_required = []
    params_optional = []
    for param in info['parameters']:
        name = param['name']
        value = param['value']
        required = param.get('required', 0)
        if name in ignore_params:
            continue
        value.strip()
        line = '%s: %s' % (name, value)
        if required:
            params_required.append(line)
        else:
            params_optional.append(line)
    params = ''
    if params_required:
        params_required.sort()
        params += '\n    Required Parameters:\n        '
        params += '\n        '.join(params_required)
    if params_optional:
        params_optional.sort()
        params += '\n    Optional Parameters:\n        '
        params += '\n        '.join(params_optional)
    context = {
        'method': method,
        'desc': desc,
        'auth': auth,
        'perms': perms,
        'params': params,
    }
    text = doc % context
    text = text.replace('<code>', "'").replace('</code>', "'")
    text = text.replace('<ul>', "").replace('</ul>', "")
    text = text.replace('<li>', " " * 12).replace('</li>', "")
    return text


class AutoDoc(type):
    def __new__(meta, classname, bases, classDict):
        selfname = classDict.get('__id__', None)
        ignore_params = ['api_key']
        for k, v in classDict.items():
            if hasattr(v, 'ipernity_method'):
                method = v.ipernity_method
                if v.static:
                    v.inner_func.__doc__ = method_doc(method, ignore_params)
                else:
                    ignore_params.append(selfname)
                    v.__doc__ = method_doc(method, ignore_params)
        return type.__new__(meta, classname, bases, classDict)
