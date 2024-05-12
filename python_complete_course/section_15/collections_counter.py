'''
Counter:
Counter is a dict subclass which helps count hashable objects.
Inside of it elements are stored as dictionary keys and the counts
of the objects are stored as the value.
'''
# Counter
from collections import Counter

# Get the number of occurrences in a list
l = [1, 1, 1, 1, 12, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
print(Counter(l))

# Get the number of occurrences in a string
s = 'ajjjjaaavvvvuuuuaaajjjvvvlll'
print(Counter(s))

# Get the number of occurrences of words in a string
s = 'How many times does each word show up in this sentence word word show up up show'
words = s.split()
print(Counter(words))

# Get the 2 most common words in the string
c = Counter(words)
print(c.most_common(2))

'''
Common uses with Counter()
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''