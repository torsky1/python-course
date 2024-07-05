a, *b = [-21, 34, 64, 123]
print(a, b)
a, *b = (-23, 54, 12, 65)
print(a, b)
a, *b = 'XYZ'
print(a, b)
a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)
a, b, *c, d = [1, 2, 3, 4, 5, 6]
print(a, b, c, d)
a, *b, c, d = 'python'
print(a, b, c, d)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l: list = [*l1, *l2]
print(l)
l1 = [1, 2, 3]
l2 = 'XYZ'
l: list = [*l1, *l2]
print(l)
#random order
s = {10, 43, 3, 'd'}
print(s)
#umpacking dict with one * returns the keys of the dict and two ** return values
a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a, b, c, d, e)
l: list = [1, 2, 3, 'python']
slic = l[0], l[1:-1], l[-1][0], l[-1][1], l[-1][2:]
print(slic)
