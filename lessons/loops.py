# FOR LOOPS
# for loops can iterate over data within lists
ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

for ninja in ninjas:
    print(ninja)

# can give for loops a range using slicing
print('-----')
for ninja in ninjas[1:3]:
    print(ninja)

# add additional logic to for loops
print('-----')
for ninja in ninjas:
    if ninja == 'yoshi':
        print(f'{ninja} - black belt')
        break
    else:
        print(ninja)
