'''
List comprehensions are a unique way of quickly creating a list with Python.
If you find yourself using a for loop along with .append() to create a list, List 
comprehensions are a good alternative
'''
# Basic way to do things
my_string = 'hello'
my_list = []
for letter in my_string:
    my_list.append(letter)
print(my_list)
# Example of how to do the same thing in list comprehensions
my_list = [letter for letter in my_string]
print(my_list)
my_list = [x for x in 'word']
print(my_list)

print()

# A few more examples
my_list = [num for num in range(0, 11)]
print(my_list)
my_list = [num**2 for num in range(0, 11)]
print(my_list)
my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)

print()

# Convert celcius to fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

print()

'''
It's worth noting that code readability is something to consider when using
list comprehensions.
'''

# If else logic
results = [x if x % 2 else 'Odd' for x in range(0, 11)]
print(results)

print()

# Basic way to do nested loops
my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        my_list.append(x * y)

print(my_list)
# List comprehensions for nested loops
my_list = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(my_list)