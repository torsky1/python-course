def func(*, d, **kwargs):
    print(d, kwargs)


func(d=4, a=3, b=1)


def func1(**kwargs):
    print(kwargs)


def func2(*args):
    print(args)


func1(a=1, b=2)
func2(1, 2)


def func3(*args, **kwargs):
    print(args, kwargs)


func3(1, 2, 4, b=100, c=123, d=3456)
