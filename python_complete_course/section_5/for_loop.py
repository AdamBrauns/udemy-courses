'''
The term iterable means you can "iterate" over the object
-i.e. iterate over a every character in a string
'''
# Basic for loop printing out the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

# If else inside of the for loop
for num in my_list:
    # Check for even numbers
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

# Getting the sum of a list
list_sum = 0

for num in my_list:
    list_sum += num

print(f'The total of the list is: {list_sum}')

# Printing each letter in a string
my_string = 'Hello World'
for letter in my_string:
    print(letter)

# When you don't intent to use the variable, use '_' as the placeholder as best practice
for _ in 'test':
    print('Coolio!')

# Printing a Tuple
tup = (1, 2, 3)
for item in tup:
    print(item)

# Tuple unpacking examples
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
    print(f'{a}\n{b}')

for a, b in my_list:
    print(f'{a}\n{b}')

# More Tuple unpacking
my_list = [(1, 2 ,3), (5, 6, 7), (8, 9, 10)]

for a, b, c in my_list:
    print(b)

# Dictionary examples
dic = {'k1':1, 'k2':2, 'k3':3}
# Only grabs the keys
for item in dic:
    print(item)
# Grabs the key value pairs
for item in dic.items():
    print(item)
# Grabs the values only 
for item in dic.values():
    print(item)

# Separate the key value pairs
for key, value in dic.items():
    print(value)