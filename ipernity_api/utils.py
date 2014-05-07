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
