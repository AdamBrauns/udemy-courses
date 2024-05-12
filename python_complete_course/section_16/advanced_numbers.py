'''
Using the function hex() you can convert numbers
into a hexadecimal format:
'''
print(hex(12))
print(hex(512))

print()

'''
Using the function bin() you can convert numbers
into their binary format.
'''
print(bin(1234))
print(bin(128))
print(bin(512))


print()
'''
The function pow() takes two arguments, equivalent
to x^y. With three arguments it is equivalent to (x^y)%z,
but may be more efficient for long integers.
'''
print(2 ** 4)
print(pow(2, 4))

print()
'''
The function abs() returns the absolute value of a number.
The argument may be an integer or a floating point number.
If the argument is a complex number, its magnitude is returned.
'''
print(abs(2))
print(abs(25))

print()
'''
The function round() will round a number to a given precision
in decimal digits (default 0 digits). It does not convert
integers to floats.
'''
print(round(3.9))
from math import pi
print(round(pi, 2))