'''
Back in Lecture 24 - Files we opened files that exist
outside of python, and streamed their contents into
an in-memory file object. You can also create in-memory
file-like objects within your program that Python treats
the same way. Text data is stored in a StringIO object,
while binary data would be stored in a BytesIO object.
This object can then be used as input or output to most
functions that would expect a standard file object.
'''
import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

print(f.read())

f.write(' \nSecond line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

print()

# Read again
print(f.read())

# Close the object when contents are no longer needed
f.close()