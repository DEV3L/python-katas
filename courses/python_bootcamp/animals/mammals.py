class Dog:
    # class variable
    breed = 'Beagle'

    # method
    def __init__(self, name):
        # instance variable
        self.name = name  # dog.name = 'fido'

    def walk(self):
        print('I am on a walk')


# function
def what_animal_am_i(animal):
    print(animal.breed)


if __name__ == '__main__':
    angela_dog = Dog('Fido')
    print(f"{angela_dog.breed} is angela's dog")

    devon_dog = Dog('Norbert')

    Dog.breed = 'Pit Bull'

    justin_dog = Dog('Epik')
    justin_dog.breed = 'Black Lab'
    # dog.type = 'Beagle'

    nick_dog = Dog('Nick')

    # what_animal_am_i(dog)
    print(f'{angela_dog.name} is of type {angela_dog.breed}')
    print(f'{devon_dog.name} is of type {devon_dog.breed}')
    print(f'{justin_dog.name} is of type {justin_dog.breed}')
    print(f'{nick_dog.name} is of type {nick_dog.breed}')
