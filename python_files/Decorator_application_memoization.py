from time import perf_counter
from functools import lru_cache


def fib(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib ({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


f = Fib()
print(f.fib(10))
print('---------------------------------')


def fib1():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib ({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib


f = fib1()
f(10)
print('-------------------------------')


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize
def fib2(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib2(n-1) + fib2(n-2)


start = perf_counter()
print(fib2(200 ))
end = perf_counter()
print(end - start)


@memoize
def fact(n):
    print('Calculating {0}'.format(n))
    return 1 if n < 2 else n * fact(n-1)


print(fact(10))
print(fact(11))


@lru_cache(maxsize=8)
def fib3(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib2(n-1) + fib2(n-2)


print(fib3(10))
print(fib3(10))

