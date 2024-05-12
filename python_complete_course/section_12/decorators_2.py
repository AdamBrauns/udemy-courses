def f1(func):
    def wrapper():
        print('Started')
        func()
        print('Ended')
    
    return wrapper

def f():
    print('Hello')

f = f1(f)

f()

print()

# Alternative (cleaner way)

def a1(func):
    def wrapper():
        print('Started')
        func()
        print('Ended')
    
    return wrapper

@a1
def a():
    print('Hello')

a()

print()

# args and kwargs

def b1(func):
    def wrapper(*args, **kwargs):
        print('Started')
        func(*args, **kwargs)
        print('Ended')
    
    return wrapper

@b1
def b(a, b=9):
    print('Hello')

b(5)

print()

# Returning values

def c1(func):
    def wrapper(*args, **kwargs):
        print('Started')
        val = func(*args, **kwargs)
        print('Ended')
        return val

    return wrapper

@c1
def add(x, y):
    return x + y

print(add(5, 7))

print()
# Method examples

import time
def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print('Run')

t = Test()
t.decorated_method()

print()
# Timer example

import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print(f'Function took: {time.time() - before} seconds')

    return wrapper

@timer
def run():
    time.sleep(2)

run()

print()
# Logging decorator
import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt', 'a') as f:
            f.write(f'Called function with {" ".join([str(arg) for arg in args])} at {str(datetime.datetime.now())}\n')
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
def run_2(a, b, c=9):
    print(a + b + c)

run_2(1, 3, 9)