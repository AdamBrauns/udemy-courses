# Assigning var to a func
def func():
    return 1

print(func())
print(func)

def hello():
    return 'Hello!'

print(hello())
print(hello)

greet = hello
greet()

del hello

# This will fail
# hello()
greet()

# -------------------
# func inside a func
def hello_2(name = 'Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello function!')

hello_2()

# -----------------------------------------
print()
# Returning a function
def hello_3(name = 'Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print('I am going to return a function!')
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello_3('Jose')
print(my_new_func)
print(my_new_func())

# -----------------------------------------
print()
# Returning a func

def cool():

    def super_cool():
        return 'I am very cool!'
    
    return super_cool

some_func = cool()
print(some_func)
print(some_func())

# -----------------------------------------
print()
# Function as an argument 

def hello_4():
    return 'Hi Jose'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello_4)

# -----------------------------------------
print()

# Creating a new decorator
def new_decorator(original_func):
    
    def wrap_func():
        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()
decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator_2():
    print('I want to be decorated')

func_needs_decorator_2()