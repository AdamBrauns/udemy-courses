'''
Problem 1:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
'''
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('An error has occurred. You provided the wrong type array.')

'''
Problem 2:
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero
'''

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('An error has occurred. You cannot divide by zero!')

'''
Problem 3:
Write a function that asks for an integer and prints the square of it. Use a while
loop with a try, except, else block to account for incorrect inputs.
'''
def square_input():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    print(f'Thank you, your number squared is: {n ** 2}')

square_input()