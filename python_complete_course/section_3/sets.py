# Sets are unordered collections of unique elements

# Creating a set and adding 1 to it
my_set = set()
my_set.add(1)
print(my_set)

# Example of adding two of the same item
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set)

# Converting a list into a set
my_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
new_set = set(my_list)
print(new_set)