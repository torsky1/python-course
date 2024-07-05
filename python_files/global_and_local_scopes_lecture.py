a = 10


def my_func(n):
    c = n ** 2
    return c


def my_func1(n):
    print('global a: ', a)
    c = a ** n
    return c


def my_func2(n):
    a = 20
    c = a ** n
    return c


def my_func3(n):
    global a
    a = 20
    c = a ** n
    return c


def my_func4():
    global var
    var = 'hello world'
    return

#NameError: name 'var' is not defined. Did you mean: 'vars'?
#print('before starting func4 ', var)


print('a before starting my_func3 a:', a)
print(my_func(2))
print(my_func1(2))
print(my_func2(2))
print(my_func3(2))
print('a after starting my_func3 a:', a)
print(my_func4())
print('printing var after starting func4 var:', var)
