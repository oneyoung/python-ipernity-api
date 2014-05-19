from functools import wraps, partial
from .methods import __methods__
from .errors import IpernityError
from .rest import call_api


def call(api_method):
    ''' decorator to wrapper api method call for instance method

    Parameters:
        api_method: Ipernity method name to be called.

    Note:
    * requirement for function:
        each function must return a tuple with (params, format_result), where
        "params" is a dict consist of parameters to ipernity api method.
        "format_result" is a function to decode json resonpse.
    * return value of decorated function:
        api json resonpse will be decoded by "format_result" function and return to caller.
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
        auth_info = info['authentication']
        # partial object for this api call
        request = partial(call_api, api_method,
                          authed=auth_info['token'],
                          http_post=auth_info['post'],
                          signed=auth_info['sign'])

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            params, format_result = func(self, *args, **kwargs)
            resp = request(**params)
            return format_result(resp)
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
        auth_info = info['authentication']
        # partial object for this api call
        request = partial(call_api, api_method,
                          authed=auth_info['token'],
                          http_post=auth_info['post'],
                          signed=auth_info['sign'])

        @wraps(func)
        def wrapper(*args, **kwargs):
            params, format_result = func(*args, **kwargs)
            resp = request(**params)
            return format_result(resp)
        return StaticCaller(wrapper)

    return decorator
