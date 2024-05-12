'''
LEGB Rule:
L:  Local - names assigned in a ny way within a function (def or lambda),
    and not declared global in that function
E:  Enclosing function locals - names in the local scope of any and all enclosing
    functions (def or lambda), from inner to outer.
G:  Global(module) - names assigned at the top-level of a module files, or declared
    global in a def within the file.
B:  Built-in (Python) - names preassigned in the built-in names module: open,
    range, SyntaxError, etc.
'''
# num is local to the lambda function
lambda num:num ** 2

# No indentation
name = 'THIS IS A GLOBAL STRING'

def greet():
    # Enclosing function local
    # If commenting this out, it will grab the global variable
    name = 'Sammy'

    def hello():
        # Local (would be first priority)
        # name = 'IM A LOCAL'
        print(f'Hello {name}')

    hello()

greet()

print()

x = 50

def func(x):
    print(f'X is {x}')

    # Local reassignment
    # This only has a scope of the function
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func(x)
# Will print 50 because the reassignment
print(x)

print()

x = 50

def func_global():
    # grab the global x
    global x
    print(f'X is {x}')

    # Local reassignment on a global variable
    # Because we grabbed global, it will change outside function
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

func_global()
# Will print 50 because the reassignment
print(x)

print()

'''
In general, it is better to avoid using the global keyword
It is cleaner and safer to do the following:
'''
x = 50

def func_avoid_global(x):
    # grab the global x
    print(f'X is {x}')

    # Local reassignment on a global variable
    # Because we grabbed global, it will change outside function
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x

x = func_avoid_global(x)
# Will print 50 because the reassignment
print(x)