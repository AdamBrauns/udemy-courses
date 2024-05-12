class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

print()
print('Creating a Dog named Niko!')
niko = Dog('Niko')
print(niko.speak())

print('Creating a Cat named Felix!')
felix = Cat('Felix')
print(felix.speak())

print()
for pet in [niko, felix]:
    print(f'{pet.name} is of type {type(pet)}')
    print(pet.speak())

print()
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)