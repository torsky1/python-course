import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=3)


def compute_powers_1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


def compute_powers_2(n, *, start=1, end):
    #using list comprehension
    return [n**i for i in range(start, end) if (n**i) % 2 == 0 and n**i is not int(False)]


def compute_powers_3(n, *, start=1, end):
    # using generators expression
    print(list(n ** i for i in range(start, end) if (n ** i) % 2 == 0 and n ** i is not int(False)))



compute_powers_1(2, end=5)
compute_powers_2(2, end=5)
compute_powers_3(2, end=5)

#print(time_it(compute_powers_1, 2, start=0, end=20000, rep=5))
#print(time_it(compute_powers_2, 2, start=0, end=20000, rep=5))
#print(time_it(compute_powers_3, 2, start=0, end=20000, rep=5))
