'''
defaultdict:
defaultdict is a dictionary-like object which provides
all methods provided by a dictionary but takes a first
argument (default_factory) as a default data type for
the dictionary. Using defaultdict is faster than doing
the same using dict.set_default method.
'''
from collections import defaultdict

# This will fail and throw a KeyError exception
# d = {}
# d['one']

# A defaultdict will simply return the default condition
d = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

# lambda function just sets it to 0
d = defaultdict(lambda : 0)
d['one']
d['two'] = 2

print(d)