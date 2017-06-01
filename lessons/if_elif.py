# OPERATORS
# <, >, =>, =<, ==, !=

# IF STATEMENT
age = int(input('Tell me your age: '))

if age < 10:
    print('Your are young, strange one')
    # any additional code for the block is tab-indented
elif age < 40:
    print('The fire in you is strong, strange one')
else:
    print('You are wise beyond doubt, strange one')

meaty = input('Do you eat meat? (y/n): ')

if meaty == 'y':
    print('here is the meaty menu...')
else:
    print('here is the veggie menu...')
