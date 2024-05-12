my_list = [1, 2, 3]

# In Python you can mix data types in lists
my_list = ['String', 100, 23.2]

print(len(my_list))
print(my_list[1:])

# Combining two lists
another_list = ['four', 'five']
combined_list = my_list + another_list
print(combined_list)

# Assigning new value
combined_list[0] = 'ONE ALL CAPS'
print(combined_list)

# Appending to list
combined_list.append('six')
print(combined_list)
combined_list.append('seven')
print(combined_list)

# Use: - del to remove an element by index 
#      - pop() to remove it by index if you need the returned value
#      - remove() to delete an element by value

combined_list.pop()
print(combined_list)

popped_item = combined_list.pop()
print(popped_item)

combined_list.pop(0)
print(combined_list)

letter_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

# This won't work, the sort doesn't return anything
my_sorted_list = letter_list.sort()
print(type(my_sorted_list))

# Sorting and reversing a list
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# List inside of a list aka listception
listception = [1, 2, [3, 4]]
print(listception[2][1])