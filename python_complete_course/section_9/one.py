def func():
    print('func() in one.py')

print('top level in one.py')

if __name__ == '__main__':
    # Run the script!
    print('one.py is being run directly')
else:
    print('one.py has been imported')
