def func1(a, b, *args):
    print("a:", a, "b:", b, "*args:", args)


l: list[int] = [10, 203, 40, 45, 54, 12, 4, 5]

func1(*l)


def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count


def avg1(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count


print(avg(2, 3, 4, 5, 6, 7, 8))
print(avg1(2, 3, 4, 5, 6, 7, 8))
