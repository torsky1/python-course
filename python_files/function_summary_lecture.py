def calc_hi_low_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (lo + hi) / 2
    if log_to_console:
        print("hi = {0}, lo={1}, avg={2}".format(hi, lo, avg))
    return avg


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

avg1 = calc_hi_low_avg(*a, log_to_console=True)
print(avg1)


def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list


store1 = []
store2 = []

add_item('apple', 2, 'units', store1)
add_item('milk',  1, "liter", store1)

print(store1)

add_item('python', 1, 'well-done', store2)
print(store2)

del store1, store2


def add_item1(name, quantity, unit=1, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list


store1 = add_item1('apple', 2)
add_item1('water', 3, store1)
print(store1)


def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)
#this func is calculating every time


print(factorial(3))


def factorial_1(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial_1(n-1, cache=cache)
        cache[n] = result
        return result


cache = {}
print(factorial_1(3, cache=cache))
del cache


def factorial_2(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial_2(n-1)
        cache[n] = result
        return result


print(factorial_2(3))
