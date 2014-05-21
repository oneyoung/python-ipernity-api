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
        m = convert_info(m)
        info[m['name']] = m
    return info


def convert_info(m):
    ''' some preprocess of method info '''
    # 'error' section contains duplicate much information, and once api call
    # failure, ipernity would response with error message, so not need to keep
    # such info.
    try:
        m.pop('errors')
        m.pop('changelog')  # changelog also unnecessary
    except KeyError:
        pass
    # some value are string, need to convert into int
    m['authentication'] = {k: int(v) if v.isdigit() else v
                           for k, v in m['authentication'].items()}
    for param in m['parameters']:
        param['required'] = int(param.get('required', 0))
    return m


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
