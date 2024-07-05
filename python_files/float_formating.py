from fractions import Fraction
from math import isclose, trunc, floor, ceil, fabs, copysign


def lesson_1():
    print(help(float))
    print(float("123.53"))
    #print(float("22/7")) u cant
    a = Fraction(22 / 7)
    print(float(a))
    print(0.1)
    print(format(0.1, ".15f"))
    print(format(0.1, ".25f"))
    print(0.125)
    print(format(0.125, ".25f"))
    a = 0.1 + 0.1 + 0.1
    b = 0.3
    print(a == b)
    print(a is b)
    print(format(a, ".25f"))
    print(format(b, ".25f"))
    print(round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5))
    print(isclose(a, b, rel_tol=1e-5, abs_tol=1e-5))
    print(isclose(2.5, 2.9))


def float_to_int():
    print(trunc(10.324),
          trunc(1234.123454213424312),
          trunc(-1231.234214))
    print(int(10.324),
          int(1234.123454213424312),
          int(-1231.234214))
    print(floor(10.324),
          floor(1234.123454213424312),
          floor(-1231.234214))
    print(ceil(10.324),
          ceil(1234.123454213424312),
          ceil(-1231.234214))


def rounding(x):
    return print(" normal round : ", round(x), "type : ", type(round(x)), "\n",
                 "round using copy sign", copysign(1, x) * int(fabs(x) + 0.5),
                 "type : ", type(copysign(1, x) * int(fabs(x) + 0.5))
                 )





