def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc


counter1 = counter()
print(counter1())
print(counter1())
print(counter1())

print('--------------------------------------------------')


def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, *kwargs)
    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_varnames)
result = counter_add(10, 30)
print(result)

counter_mult = counter(mult)
print(counter_mult.__closure__)
print(counter_mult.__code__.co_varnames)
result = counter_mult(10, 30)
print(result)

print("---------------------------------------------------------------")

counters = dict()


def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


counted_add = counter(add)
counted_mult = counter(mult)

print(counted_add(10, 20))
print(counted_mult(10, 20))
print(counted_add(10, 30))
print(counters)

print("-----------------------------------------------------\n\tfixed")


def counter(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


c = dict()

counted_add = counter(add, c)
counted_mult = counter(mult, c)

print(counted_add(10, 30))
print(counted_add(10, 30))
print(counted_add(10, 30))
print(c)

print("--------------------------------------------------\n\tfactorial func example")


def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product


print(fact(5))
print(fact(3))

counted_fact = counter(fact, c)

print(counted_fact(5))
print(c)
print(counted_fact(10))
print(c)

fact = counter(fact, c)


print(fact(3))
print(fact(10))
print(c)

add = counter(add, c)
mult = counter(mult, c)
print(add(10, 30))
print(mult(10, 30))

print(c)
