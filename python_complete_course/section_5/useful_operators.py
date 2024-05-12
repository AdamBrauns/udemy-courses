# Example of the range
my_list = [1, 2, 3]
for num in range(0, 11, 2):
    print(num)

# This is a generator (special type of function that generates 
# information instead of saving to memory)
range(0, 11, 2)
# We have to cast it to a list to get the numbers
list(range(0, 11, 2))

print()

# Example of the enumerate
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print()

'''
Note about the zip function: it will only accept the amount of the 
shortest list in the parameters. It will not error, but the rest
will be ignored.
'''
# Example of the zip function
my_list_1 = [1, 2, 3]
my_list_2 = ['a', 'b', 'c']
# Zipping the two lists together 
print(zip(my_list_1, my_list_2))

for item in zip(my_list_1, my_list_2):
    print(item)

my_list_3 = [100, 200, 300, 400, 500]
for item in zip(my_list_1, my_list_2, my_list_3):
    print(item)

zip_list = list(zip(my_list_1, my_list_2, my_list_3))
print(zip_list)

print()

# Examples of using 'in'
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('a' in 'a world')
print('mykey' in {'mykey':345})
d = {'mykey':345}
print(345 in d.values())

print()

# Getting the min and max
my_list = [10, 20, 30, 40, 100]
print(min(my_list))
print(max(my_list))

print()

# Shuffling a list
from random import shuffle

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
# This won't work because it is done on the list itself
# shuffled_list = shuffle(my_list)
shuffle(my_list)
print(my_list)

print()

# Getting a random number
from random import randint

print(randint(0, 100))
print(randint(0, 100))

print()

# This will always return a number
name = input('What is your name? ')

# This will always return a number
num = int(input('What is your favorite number? '))
print(f'Your name is {name} and your favorite number is {num}')