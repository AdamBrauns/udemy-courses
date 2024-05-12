class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

myanimal = Animal('Pikachu')
# This fails because it is not implemented
# myanimal.speak()

class Cow(Animal):

    def speak(self):
        return self.name + " says mooo!"

class Sheep(Animal):

    def speak(self):
        return self.name + " says bahhh!"

print()
print('Creating a cow named Charlie!')
charlie = Cow('Charlie')
print(charlie.speak())

print()
print('Creating a sheep named Lary!')
lary = Sheep('Lary')
print(lary.speak())