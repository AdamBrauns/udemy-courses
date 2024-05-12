'''
Three keywords:
-try: this is the block of code to be attempted (may lead to an error)
-except: block of code will execute in case there is an error in try block
-finally: a final block of code to be executed, regardless of an error
'''

def add(n1, n2):
    print(n1 + n2)

add(10, 20)

number1 = 10
#number2 = input('Please enter a number: ')
#add(number1, number2)

try:
    # Want to attempt this code
    # Might have an error
    #result = 10 + '10'
    result = 10 + 10
except:
    print('Hey, it looks like you are not adding correctly!')
else:
    print('Add went well!')
    print(result)

# Example with finally
try:
    #f = open('testfile', 'w')
    f = open('testfile', 'r')
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('There was an OS error')
except:
    # All other exceptions
    print('All other exceptions')
finally:
    print('I always run')

# Example with finally
try:
    #f = open('testfile', 'w')
    f = open('testfile', 'r')
    f.write('Write a test line')
except:
    # All other exceptions
    print('All other exceptions')
finally:
    print('I always run')

# Getting user input for a number
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops! that is not a number')
            continue
        else:
            print('Yes, thank you')
            break
        finally:
            print('I will ask you again!')

ask_for_int()