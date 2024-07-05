from html import escape
from decimal import Decimal


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_set(arg):
    return html_list(arg)


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set):
        return html_set(arg)
    else:
        return html_escape(arg)


print(htmlize(["""Python 
rocks! 0 < 1 
""", (200, 300, 400, 500), 100]))
print(htmlize([123, 456, 789]))


def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_int,
        Decimal: html_int,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict
    }

    fn = registry.get(type(arg), registry[object])

    return fn(arg)


print(htmlize(100))
