from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Func name = {0} | id = {1} | was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner


def add(a: int, b: int = 0):
    """
    Adds two values
    """
    return a + b


print("id of add func = {0}".format(id(add)))
add = counter(add)
print("id of add func = {0}".format(id(add)))

print(add(10, 30))
print(add(20, 30))


def mult(a: int, b: int, c: int = 1, *, d):
    """
    Multiplies four values
    """
    return a * b * c * d


print(mult(1, 2, 3, d=4))
mult = counter(mult)


@counter
def my_func(s: str, i: int) -> str:
    return s * i


print(my_func('a', 10))
print(help(mult))
