'''
Functions allow us to create blocks of code that can easily executed many
times, without needing to constantly rewrite the entire clock of code.
'''
def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: No input...
    OUTPUT: Hello
    '''
    print('Hello')

print(name_function)
help(name_function)
name_function()

print()

# Function with default param if no param was passed
def say_hello(name='NAME'):
    print(f'Hello {name}')

say_hello()
say_hello('John Doe')

print()

# Returning item from a function
def say_hello_return(name='NAME'):
    return f'Hello {name}'

result = say_hello_return()
print(result)
result = say_hello_return('John Doe')
print(result)

print()

# Basic math function
def add(n1, n2):
    return n1 + n2

result = add(20, 30)
print(result)

print()

# Find out if the word "dog" is in a string
def dog_check(my_string):
    return 'dog' in my_string.lower()

print(dog_check('My dog ran away'))

print()

# Pig latin function
def pig_latin(word):
    '''
    Pig Latin:
    - if a word starts with a vowel, add 'ay' to the end
    - if a word does not start with a vowel, put first letter at the end, then add 'ay'
    - word --> ordway
    - apple --> appleay
    '''
    first_letter = word[0]
    # Check if vowel
    if first_letter.lower() in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('word'))
print(pig_latin('apple'))