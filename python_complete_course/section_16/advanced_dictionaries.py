'''
Unlike some of the other Data Structures we've worked with,
most of the really useful methods available to us in Dictionaries
have already been explored throughout this course. Here we will
touch on just a few more for good measure:
'''

d = {'k1': 1, 'k2': 2}

# Dictionary comprehensions
d1 = {x:x**2 for x in range(10)}
print(d1)

d2 = {k:v**2 for k,v in zip(['a','b'],range(2))}
print(d2)

print()

print(d.values())
print(d.keys())

for k in d.values():
    print(k)