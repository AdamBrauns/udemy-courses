# Link for more formatting tips:
# https://pyformat.info/

# Formatting with the format function
print('This is a string {}'.format('INSERTED'))
print('The {2} {0} {1}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

# Float formatting follows "{value:width.precision f}"
result = 100/777
print('The result was {r:1.3f}'.format(r=result))

# f string literal found in python 3.6 
name = 'John'
print(f'Hello, his name is {name}')

name = 'Larry'
age = 5
print(f'{name} is {age} years old')