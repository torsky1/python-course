from functools import reduce

l = [5, 8, 6, 10, 9]


_max = lambda x, y: x if x > y else y


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))


_min = lambda a, b: a if a < b else b


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(min_sequence(l))


_add = lambda a, b: a+b


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l), _reduce(_min, l), _reduce(_add, l))


print(reduce(_max, l))

s = [False, 0, "a", 1]
print(reduce(lambda a, b: bool(a) and bool(b), s))


l = [1, 2, 3, 4, 5, 6, 7]


print(reduce(lambda a, b: a * b, l))


def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result


print(reduce(lambda a, b: a + b, l, 10))
