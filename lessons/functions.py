# FUNCTIONS

def greet():
    print('Hello, world')

greet()

# Parameters
def greet(name = 'ryu', time = 'morning'):
    print(f'Good {time} {name}, hope you are well?')

name = input('Your name: ')
time = input('Time of day: ')

greet(name, time)
greet()
greet(name='Yoshi')

# Something more useful
def factorial(num):
    ans = num
    i = 1
    while i < num:
        ans = ans * (num - i)
        i += 1
    print(ans)

number = int(input('Calculate factorial of: '))
factorial(number)

# 5 x 4 x 3 x 2 x 1
# 3 x 2 x 1

# Return statement
def areaCirc(radius):
    return 3.142 * radius * radius

def volCyl(area, length):
    return area * length

rad = int(input('Enter a circle radius (m): '))
len = int(input('Enter a cylinder length (m): '))
vol = volCyl(areaCirc(rad), len)

print(f'The volume of the cylinder is {vol} cubed metres')
