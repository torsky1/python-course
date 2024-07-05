help(sorted)

my_ints = (1, 65, 21, 56, 9, 19, 24, 12)
my_strings = ['D', 'B', 'c', 'a', 'E']
print(sorted(my_ints))
print(my_ints)
print(sorted(my_strings))
print(my_strings)
print(sorted(my_strings, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 123, 'xyz': 132}

for x in d:
    print(x)

print(sorted(d, key=lambda e: d[e]))


def dist_sq(value):
    return value.real**2 + value.imag**2


print(dist_sq(1 + 1j))

cmpx_list = [1+2j, 45-1j, 7+0j, 0]

# sorted(cmpx_list) you cant sort complex numbers this way right way bellow
print(sorted(cmpx_list, key=dist_sq))
# also the correct way without def a function just using lambda
print(sorted(cmpx_list, key=lambda value: value.real**2 + value.imag**2))


words_list = ['Palin', 'Cheese', 'Idle', 'Jones', 'Gilliam']
#sorting with first letter
print(sorted(words_list))
#sorting with the last letter
print(sorted(words_list, key=lambda s: s[-1]))
