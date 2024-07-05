def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)


def func1(a, b, *args):
    print(a, b, *args)


func1(1, 2, 3, 4, 5, 6)


def func2(a, b, *args, d):
    print(a, b, *args, d)


#func2(1, 2, 3, 4, 5, 6, 7, 8, 9) <- keyword arg not defined (d=....) correct code:
func2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=100)


def func3(*args, d):
    print(args, d)


func3(1, 2, 3, 4, d='abc')
#u do not need to specify *args argument
func3(d='abc')


def func4(*, d):
    print(d)


#func4(1, 2, d=100) with * do not specify positional arguments
func4(d=100)


def func5(a, b, *, d):
    print(a, b, d)


func5(1, 2, d=100)


def func6(a, b=2, *args, d):
    print(a, b, args, d)


func6(1, 3, 4, 5, 6, 7, 7, d='asdf')


