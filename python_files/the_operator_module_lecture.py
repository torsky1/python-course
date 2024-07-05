import operator
from functools import reduce
from operator import is_
print(dir(operator))
print(operator.add(1, 3))
print(operator.mul(1, 3))
print(operator.truediv(1, 3))
print(operator.floordiv(1, 3))
print(operator.lt(10, 3))

print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))
print(reduce(operator.mul, [1, 2, 3, 4]))

my_list = [1, 2, 3, 4, 5]

print(operator.getitem(my_list, 3))

operator.setitem(my_list, 1, 100)
print(my_list)
operator.delitem(my_list, 3)
print(my_list)


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print("test method running ...")


obj = MyClass()

print(obj.a, obj.b, obj.test)
