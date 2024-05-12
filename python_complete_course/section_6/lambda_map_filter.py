'''
Map will call a function for every item in a list
When calling map() the function does not need the ()
'''
def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)

list_squared = list(map(square, my_nums))
print(list_squared)

print()

def splicer(my_string):
    '''
    Return 'EVEN' if the name has an even number of characters, otherwise
    return the first letting in the name
    '''
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]

names = ['Adam', 'Larry', 'Fred']
print(list(map(splicer, names)))

print()

'''
The filter function you call must return a boolean for it to work
'''
def is_even(num):
    return num % 2 == 0

my_nums = [1, 2, 3, 4, 5, 6]
print(list(filter(is_even, my_nums)))
for n in filter(is_even, my_nums):
    print(n)

print()

'''
Lambda function annonomous function (don't give it a name or def keyword)
functionality you only want to use one time
'''
# Example of the square function above written in lambda
lambda num: num ** 2
square = lambda num: num ** 2
print(square(3))

# Square the items in the list
print(list(map(lambda num:num ** 2, my_nums)))
# Get only the even numbers
print(list(filter(lambda num:num % 2 == 0, my_nums)))
# Return the first letter of the name
print(list(map(lambda name:name[0], names)))
# Reverse each name in the list
print(list(map(lambda name:name[::-1], names)))