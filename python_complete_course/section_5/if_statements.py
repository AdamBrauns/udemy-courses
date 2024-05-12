'''
To control this flow of logic we use the keywords:
- if 
- elif
- else
'''
# Basic if statement example
hungry = True

if hungry:
    print('Feed me')
else:
    print('I am not hungry')

# Using the elif block
location = 'Bank'

if location == 'Auto Shop':
    print('Cars are cool!')
elif location == 'Bank':
    print('Money is cool')
else:
    print('I do not know your location')

# Using the else block
name = 'Adam'

if name == 'Larry':
    print('Hello Larry')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print(f'Hello {name}')