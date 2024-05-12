'''
While loops will continue to execute a block of code while some
condition remains True.
-i.e. while my pool is not full, keep filling my pool with water
'''
# You can attach an else block along with the while loop
x = 50

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print(f'x is not less than 5')

print()

'''
We can use break, continue and pass statements in our loops to 
add additional functionality for various cases. The three cases are:
- break: breaks out of the current closest enclosing loop 
- continue: goes to the top of the closest enclosing loop
- pass: does nothing at all
'''
# Example of pass
x = [1, 2, 3]
for item in x:
    pass

# Example of continue
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue    
    print(letter)

print()

# Example of break
for letter in my_string:
    if letter == 'a':
        break
    print(letter)

print()

# Another break example
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1