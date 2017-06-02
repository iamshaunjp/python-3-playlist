class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print('Planet stats:')
print(f'Name: {hoth.name}')
print(f'System: {hoth.system}')
print(hoth.orbit())

naboo= Planet('Naboo', 300000, 8, 'Naboo System')
print('Planet stats:')
print(f'Name: {naboo.name}')
print(f'System: {naboo.system}')
print(naboo.orbit())
