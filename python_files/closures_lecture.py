def outer():
    x = 'python'

    def inner():
        print(x)
    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)


def outer1():
    x = [1, 2, 3]
    print(hex(id(x)))

    def inner():
        y = x
        print(hex(id(y)))
    return inner


fn = outer1()
fn()


def outer3():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count
    return inc


fn = outer3()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))
print(fn())
print(fn.__closure__)
print(fn())


def outer4():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2


fn1, fn2 = outer4()

print(fn1.__code__.co_freevars)
print(fn2.__code__.co_varnames)
print(fn1.__closure__)
print(fn2.__closure__)
print('running fn1() ... count : ', fn1())
print(fn1.__closure__)
print(fn2.__closure__)
print('running fn2() ... count : ', fn2())
print(fn1.__closure__)
print(fn2.__closure__)
print('----------------------------------------------------\npower func')


def power(n):
    def inner(x):
        return x ** n
    return inner


square = power(2)
print(square.__closure__)
print(hex(id(2)))
print(square)
print('5^2', square(5))
cube = power(3)
print(cube.__closure__)
print('5^3', cube(5))
print('-------------------------------------------\nadder')


def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__closure__, '\n', add_2.__closure__, '\n', add_3.__closure__)

print('1 + 10 add_1(10)', add_1(10))
print('2 + 10 add_1(10)', add_2(10))
print('3 + 10 add_1(10)', add_3(10))

print('-----------------------------------------\nadders with list')
#adders = []
#for n in range(1, 4):
  #  adders.append(lambda x: x + n)

#print(adders)
#print(n)
#print(adders[0](10))

print('-----------------------------------------\nadders list in func')
#common n (3 in this case) in closures


def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders


adders1 = create_adders()
print(adders1)
print(adders1[0].__closure__)
print(adders1[1].__closure__)
print(adders1[0](10))
print(adders1[1](10))
print(adders1[2](10))
print('-----------------------------------------\nadders func fixed bug')
#it's not closure no free variable


def create_adders1():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x + y)
    return adders


adders2 = create_adders1()
print(adders2[0](10))
print(adders2[1](10))
print(adders2[2](10))
