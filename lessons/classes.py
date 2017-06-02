class Planet:

    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()
print('Planet stats:')
print(f'Name: {hoth.name}')
print(f'System: {hoth.system}')
print(hoth.orbit())
