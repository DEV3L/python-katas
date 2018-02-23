# a class encapsulates behavior and state
value = 1


class Hat:
    def __init__(self, style: str):
        self.style = style

    def __str__(self):
        return self.style


def a_function():
    print(1)


hat1 = Hat('beanie')
hat2 = Hat('sports cap')
hat3 = Hat('fedora')

hats = [hat1, hat2, hat3]

for hat in hats:
    print(hat)


class Adventurer:
    def __init__(self, name: str, equipment: dict):
        self.name = name
        self.hat = equipment['hat']
        self.shoes = equipment['shoes']

    def __str__(self):
        return f'I am {self.name}. I wear {self.hat} hat and {self.shoes} shoes'


default_equipment = {
    'hat': Hat('peasant'),
    'shoes': None
}

sara = Adventurer('sara', default_equipment)

print(sara)

# adventure adventure adventure

# sara finds a steel visor
sara.hat = Hat('steel visor')

print(sara)

x = 5
y = 4

grid = []

for x_count in range(x):
    grid.append([])
    for y_count in range(y):
        grid[x - 1].append('x')

print(grid)
