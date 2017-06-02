def belt_count(dict):
    belts = list(dict.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

# def ninja_intro(dict):
#     for key, val in dict.items():
#         print(f'I am {key} and I am a {val} belt')

ninja_belts = { }

while True:
    ninja_name = input('add a ninja name: ')
    ninja_belt = input('add a ninja colour: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n): ')
    if another == 'y':
        continue
    else:
        break

# ninja_intro(ninja_belts)
belt_count(ninja_belts)
