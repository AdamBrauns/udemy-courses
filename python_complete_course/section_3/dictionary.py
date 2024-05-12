# Declaring a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])

# Example
price_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(price_lookup['apple'])

# Example of dictionary and key inside a dictionary
d = {'k1': 123, 'k2':[0, 1, 2], 'k3':{'insideKey': 100}}
print(d)
print(d['k2'][2])
print(d['k3']['insideKey'])

# Example of making an item upper case inside the dictionary
d = {'key1': ['a', 'b', 'c']}
my_list = d['key1']
letter = my_list[2]
print(letter.upper())
print(d['key1'][2].upper())

# Assigning new values
d = {'k1': 100, 'k2': 200}
print(d)
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)

# Other useful methods
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
# Returns a tuple
print(d.items())