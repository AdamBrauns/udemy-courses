'''
In this series of lectures we will be diving a little
deeper into all the methods available in a list object.
These aren't officially "advanced" features, just methods
that you wouldn't typically encounter without some additional
exploring. It's pretty likely that you've already encountered
some of these yourself!
'''
l = [1,2,3]
# Merely appends an element to the end of a list:
l.append(4)
print(l)

print()
# count() takes in an element and returns the number
# of times it occurs in your list:
print(l.count(10))
print(l.count(2))

print()
# append: appends whole object at end:
x = [1, 2, 3]
x.append([4, 5])
print(x)

print()
# extend: extends list by appending elements from the iterable:
x = [1, 2, 3]
x.extend([4, 5])
print(x)

print()
# index() will return the index of whatever element is placed as
# an argument. Note: If the the element is not in the list an error
# is raised.
print(l.index(2))
# This will fail
# print(l.index(12))

print()
# insert() takes in two arguments: insert(index,object) This method
# places the object at the index supplied. For example:
l.insert(2, 'inserted')
print(l)

print()
# You most likely have already seen pop(), which allows us to "pop" off
# the last element of a list. However, by passing an index position you
# can remove and return a specific element.

# pop off the second item
ele = l.pop(1)
print(ele)

print()
# The remove() method removes the first occurrence of a value. For example:
l.remove('inserted')
print(l)

print()
# As you might have guessed, reverse() reverses a list. Note this occurs in place!
# Meaning it affects your list permanently.

l.reverse()
print(l)

print()
# The sort() method will sort your list in place:
l.sort()
print(l)
# The sort() method takes an optional argument for reverse sorting. Note this is
# different than simply reversing the order of items.
l.sort(reverse=True)
print(l)

print()
'''
A common programming mistake is to assume you can assign a modified list to a new
variable. While this typically works with immutable objects like strings and tuples:
'''
x = 'hello world'
y = x.upper()
print(y)
# HELLO WORLD
# This will NOT work the same way with lists:
x = [1,2,3]
y = x.append(4)
print(y)
'''
What happened? In this case, since list methods like append() affect the list
in-place, the operation returns a None value. This is what was passed to y. In
order to retain x you would have to assign a copy of x to y, and then modify y:
'''
print()

x = [1,2,3]
y = x.copy()
y.append(4)
print(x)
print(y)