class Animal():

    def __init__(self):
        print("Animal created")
    
    def who_am_i(self):
        print('I am an animal!')
    
    def eat(self):
        print('I am eating!')

myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()

print()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")
        
    def eat(self):
        print('I am a dog and I am eating!')

    def bark(self):
        print("Woof!")

mydog = Dog()
mydog.who_am_i()
mydog.eat()