# Problem 1
def gensquares(N):
    '''
    Create a generator that generates the squares of numbers up to some number N.
    '''
    for num in range(N):
        yield num ** 2


for x in gensquares(10):
    print(x)

'''
output:
0
1
4
9
16
25
36
49
64
81
'''

print()

# Problem 2:
import random

random.randint(1,10)

def rand_num(low, high, n):
    '''
    Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
    Note: Use the random library. For example:
    '''
    for _ in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

'''
output:
6
1
10
5
8
2
8
5
4
5
1
4
'''

print()

# Problem 3
'''
Use the iter() function to convert the string below into an iterator:
'''

s = 'hello'
s = iter(s)
print(next(s))

# Problem 4
'''
Explain a use case for a generator using a yield statement where you would
not want to use a normal function with a return statement.
'''

'''
Answer:

If the output has the potential of taking up a large amount of memory and you only indend to iterate
through it, you would want to use a generator.
'''

# Problem 5 (Extra credit)
'''
Can you explain what gencomp is in the code below? (Note: We never covered
this in lecture! You will have to do some Googling/Stack Overflowing!)
Hint: Google generator comprehension!
'''
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

'''
output:
4
5
'''

'''
Answer:

It's like list comprehension but for generators. It doesn't create the list in memory.
All you have to do is swap the [] for () and you have a generator comprehension
'''