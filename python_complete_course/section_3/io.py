my_file = open('myfile.txt')
# This will fail because the file does not exist
# my_file = open('whoops.txt')

# Returns the giant string of the text file
print(my_file.read())

# This will return an empty string
# We need to reset the curser to 0 to read it again
print(my_file.read())

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
contents = my_file.read()
print(contents)

# Returns a list where each element is a line
my_file.seek(0)
print(my_file.readlines())

# Best practice is to close it in order to not get any errors
my_file.close()

# By using this way, you no longer have to worry about closing the file
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

# Mode: r = read only
#       a = append only
#       w = write only (overwrites an existing file or creates new)
#       r+ = reading and writing
#       w+ = writing and reading (overwrites an existing file or creates new)
with open('myfile.txt', mode = 'a') as f:
    f.write('\nFOUR ON FOURTH')
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

# Writing to a file name
with open('game.txt', mode = 'w') as f:
    f.write('Fortnite bad, Minecraft good')
with open('game.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)