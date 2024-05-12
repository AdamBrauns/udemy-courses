'''
OrderedDict
An OrderedDict is a dictionary subclass that remembers the
order in which its contents are added.
'''

# Order does not matter 
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)

print()

from collections import OrderedDict

# Order matters
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)

print()

# Normal dict check will be true because they have the same contents

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

# OrderedDict check will be false because they were added in a different order

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)