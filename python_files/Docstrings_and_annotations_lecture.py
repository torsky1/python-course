def my_func(a):
    """documentation of my func"""
    return a


print(help(my_func))
#the documentation of the func is stored in __doc__
print(my_func.__doc__)


def my_func1(a: 'a string', b: 'positive int number') -> 'a string':
    return a*b


print(help(my_func1))
#in this case __doc__ is empty
print(my_func1.__doc__)


def my_func2(a: str, b: 'int > 0') -> str:
    return a*b


print(help(my_func2))

x = 3
y = 5


def my_func3(a: str) -> 'a repeated ' + str(max(x, y)) + ' times':
    """some documentation"""
    return a*max(x, y)


print(help(my_func3))
#the annotations are stored in __annotations__
print(my_func3.__annotations__)
print(my_func3.__doc__)
