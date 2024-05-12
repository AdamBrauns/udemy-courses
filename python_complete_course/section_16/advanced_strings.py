s = 'hello world'

print(s.capitalize())
print(s.upper())
print(s.lower())
# Returns the number of occurrences, without overlap
print(s.count('o'))
# Returns the starting index position of the first occurrence
print(s.find('o'))

'''
The center() method allows you to place your string 'centered'
between a provided string with a certain length. Personally,
I've never actually used this in code as it seems pretty esoteric...
'''
print(s.center(20, 'z'))

# The expandtabs() method will expand tab notations \t into spaces:
print('hello\thi'.expandtabs())

print()

s = 'hello'
print(f'The string we are checking is {s}')

# isalnum() will return True if all characters in s are alphanumeric
print(f'isalnum: {s.isalnum()}')

# isalpha() will return True if all characters in s are alphabetic
print(f'isaplha: {s.isalpha()}')

# islower() will return True if all cased characters in s are lowercase
# and there is at least one cased character in s, False otherwise.
print(f'islower: {s.islower()}')

# isspace() will return True if all characters in s are whitespace.
print(f'isspace: {s.isspace()}')

# istitle() will return True if s is a title cased string and there
# is at least one character in s, i.e. uppercase characters may only
# follow uncased characters and lowercase characters only cased ones.
# It returns False otherwise.
print(f'istitle: {s.istitle()}')

# isupper() will return True if all cased characters in s are uppercase
# and there is at least one cased character in s, False otherwise.
print(f'isupper: {s.isupper()}')

# Another method is endswith() which is essentially the same as a boolean check on s[-1]
print(f'endswith: {s.endswith("o")}')

print()
'''
Strings have some built-in methods that can resemble regular expression
operations. We can use split() to split the string at a certain element
and return a list of the results. We can use partition() to return a
tuple that includes the first occurrence of the separator sandwiched
between the first half and the end half.
'''
print(s.split('e'))
print(s.partition('l'))