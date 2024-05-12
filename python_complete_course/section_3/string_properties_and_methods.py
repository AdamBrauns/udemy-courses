name = 'Sam'
# This will fail because strings don't support item assignment
# name[0] = 'P'

last_letters = name[1:]
new_name = 'P' + last_letters
x = 'Hello World'
x += " it is beautiful outside!"

letter = 'xy'
letter *= 10
print(letter)

print(2 + 3)
print('2' + '3')
# Can't do this 
# print(2 + '3')

x = 'Hello World'
xupper = x.upper()
xlower = x.lower()
x.split()
x = 'Hi this is a string'
x.split('i')