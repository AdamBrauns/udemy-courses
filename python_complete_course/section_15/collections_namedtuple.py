'''
namedtuple
The standard tuple uses numerical indexes to access its members.
'''
t = (1,2,3)
print(t[0])

from collections import namedtuple

# Dog example
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
print(sam)
print(sam.age)
print(sam.breed)
print(sam.name)
# Can also call by index
print(sam[0])

print()

# Cat example
Cat = namedtuple('Cat', 'fur claws name')
kitty = Cat(fur='Fuzzy', claws=False, name='Kitty')
print(kitty)
print(kitty.fur)
print(kitty.claws)
print(kitty.name)
# Can also call by index
print(kitty[0])