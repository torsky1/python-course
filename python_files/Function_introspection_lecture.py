import inspect
from inspect import isfunction, ismethod, isroutine


def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=3,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=1000,
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """
    This function does nothing just have some parameters and annotations.
    """
    i = 10
    j = 20
    a = i + j
    return a


my_func.short_description = "This is a func that does nothing"

print(my_func.__doc__)
print(my_func.__annotations__)
print(my_func.short_description)
print(dir(my_func))
print(my_func.__name__)

print(id(my_func))


def func_call(f):
    print(id(f))
    print(f.__name__)


func_call(my_func)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
#argcount shows only positional arguments (first 3 in this case)
print(my_func.__code__.co_argcount)


a = 10
print(isfunction(a))
print(ismethod(my_func))


class MyClass:
    def f(self):
        pass


print(isfunction(MyClass.f))
my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(my_obj.f))
print(inspect.getsource(my_func))
