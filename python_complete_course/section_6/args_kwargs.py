# Basic function
def my_func(a, b):
    '''
    Returns 5% of the sum of a and b
    '''
    return sum((a, b)) * 0.05

print(my_func(40, 60))

print()

# Same as the example above with optional 3rd param
def my_func_option_c(a, b, c=0):
    '''
    Returns 5% of the sum of a and b
    '''
    return sum((a, b, c)) * 0.05

print(my_func_option_c(40, 60))

'''
The *args allows you to add any number of args into a function
allowing the code to be more flexible. 
'''
def my_func_args(*args):
    return sum(args) * 0.5

print(my_func_args(40, 60, 80, 100))

def my_func_args_print(*args):
    print(args)

my_func_args_print(40, 60, 80, 100)

'''
Worth noting that args is an arbitrary name. You could pass in
another keyword, however, args is used for standardization.
def my_func_args_print(*spam):
    print(spam)
'''

print()

'''
The **kwargs acts similar to *args, however, it passes a dictionary
into the function (Keyword Arguments)
'''
def my_func_kwargs(**kwargs):
    if 'fruit' in kwargs:
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print('I did not find any fruit here')

my_func_kwargs(fruit = 'apple', veggie = 'lettuce')

def my_func_kwargs_print(**kwargs):
    print(kwargs)

my_func_kwargs_print(fruit = 'apple', veggie = 'lettuce')

'''
Worth noting that args is an arbitrary name. You could pass in
another keyword, however, args is used for standardization.
def my_func_args_print(**jelly):
    print(jelly)
'''

print()

def my_func_both(*args, **kwargs):
    print(f'I would like {args[0]} {kwargs["food"]}')

my_func_both(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dog')

'''
You cannot pass args out of order, you must pass them in as the order
you specify in the function.
Example:
def my_func_both(*args, **kwargs):
    print(f'I would like {args[0]} {kwargs["food"]}')

my_func_both(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dog', 10)
'''