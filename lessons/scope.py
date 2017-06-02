my_name = 'ryu'

def print_name():
    global my_name
    my_name = 'yoshi'
    print('inside the function the name is', my_name)
    print(locals().keys())
    print(globals().keys())

print_name()
print('outside the function the name is', my_name)
