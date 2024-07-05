list_num = [2, 3, 4]
num1 = [1, 2, 3]
num2 = [10, 20, 30]

#the map function


def sq(x):
    return x ** 2


def add(x, y):
    return x + y


print(list(map(sq, list_num)))
print(list(map(add, num1, num2)))
print(list(map(lambda x, y: x + y, num1, num2)))
print(help(map))


#the filter function

list_02 = [0, 1, 2, 3, 4]

print(list(filter(None, list_02)))


def is_even(n):
    return n % 2 == 0


print(filter(is_even, list_02))
print(filter(lambda x: x % 2 == 0, list_02))


#the zip function

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
l3 = ['a', 'b', 'c', 'd', 'e']


print(list(zip(l1, l2, l3)))


#the list comprehension alternative to map


def sq(x):
    return x**2


print(list(map(sq, l1)))

result = []
for x in l1:
    result.append(x**2)

print(result)

print([x**2 for x in l1])

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30]

print([x + y for x, y in zip(l1, l2)])

print(list(filter(lambda n: n % 2 == 0, l1)))
print([x for x in l1 if x % 2 == 0])


lisran = range(10)
print(list(filter(lambda y: y < 25, map(lambda x: x**2, lisran))))
#easier way of doing it
print([x**2 for x in range(10) if x**2 < 25])

