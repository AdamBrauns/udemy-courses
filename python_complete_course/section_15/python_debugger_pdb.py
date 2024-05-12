'''
You've probably used a variety of print statements to try to
find errors in your code. A better way of doing this is by using
Python's built-in debugger module (pdb). The pdb module implements
an interactive debugging environment for Python programs. It includes
features to let you pause your program, look at the values of variables,
and watch program execution step-by-step, so you can understand what
your program actually does and find bugs in the logic.

This is a bit difficult to show since it requires creating an error
on purpose, but hopefully this simple example illustrates the power
of the pdb module.
'''
import pdb

x = [1, 2, 3, 4]
y = 2
z = 3

result = y + z
print(result)

# Brings up an interactive menu to debug code
# Enter 'q' to quit the terminal
pdb.set_trace()

result2 = y + x
print(result2)