def ninja_intro(dict):
    for key, val in dict.items():
        print(f'I am {key} and I am a {val} belt')

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

ninja_intro(ninja_belts)
