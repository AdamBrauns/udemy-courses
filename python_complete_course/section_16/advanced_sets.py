s = set()

s.add(1)
s.add(2)
s.add(2)

print(f'Set s = {s}')

print()

s.clear()

print(f's after clear: {s}')

print()
'''
returns a copy of the set. Note it is a copy, so changes to the
original don't effect the copy.
'''
s = {1, 2, 3}
sc = s.copy()

# difference returns the difference of two or more sets
sc.add(4)
print(s)
print(sc)
print(f'The difference is {sc.difference(s)}')

print()

# the method returns set1 after removing elements found in set2
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(f'Difference update: {s1}')

print()

# Removes an element from a set if it is a member. If the element is not a member, do nothing.
s = {1, 2, 3, 4}
s.discard(1)
# You won't get an error trying to remove item not in set
s.discard(12)
print(s)

print()
'''
Returns the intersection of two or more sets as a new set.
(i.e. elements that are common to all of the sets.)
'''
print(f'Intersection: ')
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

print()

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# This method will return True if two sets have a null intersection.
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
# This method reports whether another set contains this set.
print(s1.issubset(s2))
# This method will report whether this set contains another set. Inverse of subset
print(s2.issuperset(s1))
# Return the symmetric difference of two sets as a new set.(i.e. all elements
# that are in exactly one of the sets.)
print(s1.symmetric_difference(s2))
# Returns the union of two sets (i.e. all elements that are in either set.)
print(s1.union(s2))
# Update a set with the union of itself and others.
s1.update(s2)
print(s1)