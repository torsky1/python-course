from functools import partial


def my_func(a, b, c):
    print(a, b, c)


def fn(b, c):
    return my_func(10, b, c)


print(fn(20, 30))

f = lambda x, y: my_func(10, x, y)
