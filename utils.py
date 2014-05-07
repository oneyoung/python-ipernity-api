from ipernity_api import rest


def dict2code(d, indent=''):
    ''' convert json decoded dict into python literal code

    Parameters:
        d: dict to be converted
        indent: optinal parameter for base indent of code segment
    '''
    tab = '    '
    prefix = indent  # tab indent mark
    code = ''  # result
    for c in str(d):
        if c == '{':
            code += '{\n' + prefix
            prefix += tab
        elif c == '}':
            code += '\n' + prefix + '}\n' + prefix
            prefix = prefix[:-len(tab)]
        else:
            code += c

    return code


def get_methods_list():
    ''' return all the methods' name as a list '''
    resp = rest.call_api('api.methods.getList')
    methods = [m['name'] for m in resp['methods']['method']]
    methods.sort()
    return methods


def get_methods_info():
    ''' get detail about each method, and return a dict with method name as key '''
    info = {}
    for method in get_methods_list():
        resp = rest.call_api('api.methods.get', http_post=False, method=method)
        m = resp['method']
        info[m['name']] = m
    return info


def create_methods_file(filename='methods.py'):
    ''' save methods info to file '''
    methods_info = get_methods_info()
    code = dict2code(methods_info)
    buf = "__methods__ = %s" % code
    f = open(filename, 'w')
    f.write(buf)
    f.close()


if __name__ == '__main__':
    create_methods_file('ipernity_api/methods.py')
