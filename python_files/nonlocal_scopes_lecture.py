def outer_func():
    x = 'hello'

    def inner_func():
        print(x)
    inner_func()


print(outer_func())


def outer_func1():
    x = 'hello'

    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()


outer_func1()


def outer_func2():
    x = 'hello'

    def inner():
        x = 'python'
        print('inner :', x)
    inner()
    print('outer :', x)


outer_func2()


def outer_func3():
    x = 'hello'

    def inner():
        nonlocal x
        x = 'python'
        print('inner1 :', x)
    inner()
    print('outer1 :', x)


outer_func3()


def outer_func4():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()

