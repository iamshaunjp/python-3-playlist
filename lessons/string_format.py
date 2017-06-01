num1 = 3.14523678
num2 = 10.2903948

# PREVIOUS WAY
# opening and closing strings, no formatting options
print('num 1 is', num1, 'and num2 is', num2)

# FORMAT METHOD
# order important, first number is the index, : specifies formatting options
print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2))

# USING F-STRING
# no ordering, colon specifies formatting options
print(f'num1 is {num1:.3f} and num2 is {num2:.3f}')

# FILE SYSTEM EXAMPLE
folder = 'Sandbox'
print(fr'C:\User\Documents\{folder}')
