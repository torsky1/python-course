lambda x: x**2


print(type(lambda x: x**2))

f = lambda x, y: x+y

print(f(3, 45))


def apply_func(x, fn):
    return fn(x)


print(apply_func(7, lambda x: x**2))


def apply_func_1(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply_func_1(lambda x: x**2, 6))

print(apply_func_1(lambda x, y: (x**2)+(y**2), 2, 3))

print(apply_func_1(lambda x, *, y: (x**2)+(y**2), 2, y=20))

print(apply_func_1(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(apply_func_1(sum, (1, 2, 3, 4, 5)))
