'''
Generators allow us to generate a sequence of values over time
The main difference in syntax will be the use of a yield statement
The advantage is that instead of having to compute an entire series of values up
front, the generator computes one value, waits until the next value is called for
An example is the range() function:
    - It just keeps track of the last number and the step size to provide a
      flow of numbers
'''
# Without generators, we have to store the item in memory
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result

print(create_cubes(10))
for x in create_cubes(10):
    print(x)

print()

# With generators, we do not have to store the entire list
def create_cubes_gen(n):
    for x in range(n):
        yield x ** 3

print(create_cubes_gen(10))
for x in create_cubes_gen(10):
    print(x)

print()

# Fibonacci series generator
def gen_fib(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in gen_fib(10):
    print(number)

print()

# Example with the next iterator
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
# This will throw a StopIteration error because it doesn't have another one
# The for loop already catching this exception
# print(next(g))

print()
# String iteration example

s = 'hello'
for letter in s:
    print(letter)

print()
# This will fail because you can't use next with string by default
# next(s)

# Make it iterable by using the iter() function
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
