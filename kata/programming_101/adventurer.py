import random


class Adventurer:
    def __init__(self, map, name, strength):
        self.map = map
        self.name = name
        self.strength = strength

    def receive_map(self, other_adventurer):
        other_map = other_adventurer.map
        self.map = other_map


def generate_character(map, name):
    strength = random.randint(1, 18)
    adventurer = Adventurer(map, name, strength)
    return adventurer


good_map = 'good map'
bad_map = 'bad map'

justin = generate_character(bad_map, 'justin')
alex = generate_character(good_map, 'alex')
sara = generate_character(bad_map, 'sara')
grande = generate_character(good_map, 'grande')

party = [justin, alex, sara, grande]

for adventurer in party:
    print(adventurer.name + '-' + adventurer.map + ':' + str(adventurer.strength))
