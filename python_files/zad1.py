def func(a, b):
    x = a // b
    y = a % b
    z = a/b
    print(a, "/", b, "=", z)
    print("a//b = ", x)
    print("a%b = ", y)
    print("a = ", b, "*", x, "+", y, "=", b * x + y)


func(int('0b1011', base=2), 5)
