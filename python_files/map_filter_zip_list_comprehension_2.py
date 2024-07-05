def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))

print(list(map(fact, range(6))))

print(list(filter(lambda x: x % 3 == 0, range(28))))

print(list(filter(None, [1, 0, 3, 2, 5, 'a', '', None, True, False])))


l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = ('python')

results = list(zip(l1, l2, l3))
for x in results:
    print(x)

print(results)

print(list(zip(range(10000), 'python')))

print([x+y for x, y in zip(l1, l2)])

l = range(10)

print(list(l))

print(list(map(fact, l)))

print([fact(n) for n in l])

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [10, 20, 30, 40, 50]

print(list(map(lambda x, y: x+y, l1, l2)))

print([x+y for x, y in zip(l1, l2)])
print([x+y for x, y in zip(l1, l2) if (x+y) % 2 == 0])
