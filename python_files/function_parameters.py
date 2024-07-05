#def my_func(a, b, c):
#  print("a = {0}, b = {1}, c = {2}".format(a, b, c))


#def my_func1(a, b=2, c=3):
#  print("a = {0}, b = {1}, c = {2}".format(a, b, c))


#tuples


a = (1, 2, 3)
b = 1, 2, 3
c = (1,)

#unpacking

d, e, f = 1, 2, 3

#(a, b, c) = [1, {1, 3, 4}, [1, 5, 74, "a"]]

#temp swap

#a, b = [10, 20]

#print(a, b)

(a, b) = (b, a)

#print(a, b)

#unpacking
for e in "xyz":
    print(e)

e = {"a": 1, "b": 2, "c": 3}
print(e)
e.pop("c", 3)
