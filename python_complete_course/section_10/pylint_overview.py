'''
There are several testing tools, we will focus on two:
-pylint: this is a library that looks at your code and reports 
back possible issues (PEP 8)
-unittest: This built-in library will allow to test your own
programs and check you are getting desired outputs

Run pylint by using: 'pylint <python file>'
It returns a rating out of 10 where 10 is the best
'''

def my_func():
    '''
    A simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)

my_func()