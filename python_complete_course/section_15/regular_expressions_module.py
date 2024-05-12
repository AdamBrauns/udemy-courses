'''
Regular expressions are text-matching patterns described
with a formal syntax. You'll often hear regular expressions
referred to as 'regex' or 'regexp' in conversation. Regular
expressions can include a variety of rules, from finding
repetition, to text-matching, and much more. As you advance
in Python you'll see that a lot of your parsing problems can
be solved with regular expressions (they're also a common interview question!).

If you're familiar with Perl, you'll notice that the syntax
for regular expressions are very similar in Python. We will
be using the re module with Python for this lecture.
'''
import re

patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "{}" in:\n "{}"\n'.format(pattern,text))
    
    #Check for match
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')
print()

print(re.search('h', 'w'))

print()

match = re.search(patterns[0], text)
print(type(match))

print()

# Where the match starts and ends
print(match.start())
print(match.end())

print()

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
print(re.split(split_term, phrase))

# Similar to doing:
print(phrase.split('@'))

print()

find_all = re.findall('match', 'Here is one match, here is another match')
print(find_all)
print(f'There are {len(find_all)} occurrences.')

print()

def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

print()

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns, test_phrase)

print()

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!.? ]+', test_phrase))

print()

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns, test_phrase)

print()

'''
Escape Codes
Code	Meaning
\d	    a digit
\D	    a non-digit
\s	    whitespace (tab, space, newline, etc.)
\S	    non-whitespace
\w	    alphanumeric
\W	    non-alphanumeric
'''

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)