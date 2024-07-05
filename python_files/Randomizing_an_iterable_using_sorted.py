import random

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my sollution
print(sorted(my_numbers, key=lambda x: my_numbers[random.randint(0, 9)]))
#the course guy sollution
print(sorted(my_numbers, key=lambda x: random.random()))
