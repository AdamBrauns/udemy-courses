t = (1, 2, 3)
my_list = [1, 2, 3]
print(type(t))
print(type(my_list))

t = ('one', 2)
print(t[0])
print(t[-1])

t = ('a', 'a', 'b')
# Counts how many occurrences 
print(t.count('a'))
# grabs the first occurrence of the param
print(t.index('a'))

my_list[0] = 'NEW'
print(my_list)

# This will fail because tuples are immutable
# Tuples are good for data integrity 
# t[0] = 'NEW'