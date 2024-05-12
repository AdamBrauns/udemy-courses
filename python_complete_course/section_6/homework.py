# Problem 1
def vol(rad):
    '''
    Write a function that computes the volume of a sphere given its radius.
    '''
    return (4/3) * 3.14 * (rad**3)

print()
print('Problem 1')
print('------------')
print(vol(2))
print()

'''
output:
33.493333333
'''

# Problem 2
def ran_check(num,low,high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    if num > low and num < high:
        return f'{num} is in the range between {low} and {high}'
    return f'{num} is not in the range between {low} and {high}'
print('Problem 2(a)')
print('------------')
print(ran_check(5, 2, 7))
print()

'''
output:
5 is in the range between 2 and 7
'''

# Boolean
def ran_bool(num,low,high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    return num > low and num < high
print('Problem 2(b)')
print('------------')
print(ran_bool(3,1,10))
print()

'''
output: 
True
'''

# Problem 3
def up_low(s):
    '''
    Write a Python function that accepts a string and calculates the
    number of upper case letters and lower case letters.
    '''
    upr_lowr = {'up': 0, 'low': 0}
    for letter in s:
        if letter.isupper():
            upr_lowr['up'] += 1
        elif letter.islower():
            upr_lowr['low'] += 1
    return f'No. of Upper case characters : {upr_lowr["up"]}\nNo. of Lower case characters : {upr_lowr["low"]}'

print('Problem 3')
print('------------')
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
print()

'''
output:
Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
No. of Upper case characters :  4
No. of Lower case Characters :  33
'''

# Problem 4
def unique_list(lst):
    '''
    Write a Python function that takes a list and returns a new list
    with unique elements of the first list.
    '''
    return list(set(lst))

print('Problem 4')
print('------------')
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print()

'''
output:
[1, 2, 3, 4, 5]
'''

# Problem 5
def multiply(numbers):
    '''
    Write a Python function to multiply all the numbers in a list.
    ''' 
    total = 1
    for num in numbers:
        total *= num
    return total

print('Problem 5')
print('------------')
print(multiply([1,2,3,-4]))
print()

'''
output:
-24
'''

# Problem 6
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(s):
    '''
    Write a Python function that checks whether a passed in string is palindrome or not.
    '''
    return s == s[::-1]

print('Problem 6')
print('------------')
print(palindrome('helleh'))
print()

'''
output:
True
'''
# Problem 7
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    '''
    Write a Python function to check whether a string is pangram or not.
    '''
    return set(alphabet) <= set(str1.lower())

print('Problem 7')
print('------------')
print(ispangram("The quick brown fox jumps over the lazy dog"))
print()

'''
output:
True
'''