'''
Sometimes it's important to know how long your code is
taking to run, or at least know if a particular line of
code is slowing down your entire project. Python has a
built-in timing module to do this.

This module provides a simple way to time small bits of
Python code. It has both a Command-Line Interface as well
as a callable one. It avoids a number of common traps for
measuring execution times.Sometimes it's important to know
how long your code is taking to run, or at least know if
a particular line of code is slowing down your entire project.
Python has a built-in timing module to do this.

This module provides a simple way to time small bits of
Python code. It has both a Command-Line Interface as well
as a callable one. It avoids a number of common traps for
measuring execution times.
'''
import timeit

# '0-1-2-3-...-99'
print(timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000))

print(timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000))

print(timeit.timeit("'-'.join(map(str, range(100)))", number=10000))