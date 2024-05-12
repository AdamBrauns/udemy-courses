class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self, number):
        print('WOOF! My name is {} and I am number: {}'.format(self.name, number))

print('\nCreating Dog number 1')
my_dog = Dog(breed='Poodle', name='Cooper', spots=False)
my_dog.bark(1)

print('\nCreating Dog number 2')
my_dog2 = Dog(breed='Lab', name='Sam', spots=False)
my_dog2.bark(2)

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
    
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print('\nCreating a circle object with a radius of the default: {}'.format(my_circle.radius))
print('Circle radius: {}'.format(my_circle.area))
print('Circle circumference: {}'.format(my_circle.get_circumference()))

radius = 30
my_circle = Circle(radius)
print('\nCreating a circle object with a radius of: {}'.format(radius))
print('Circle radius: {}'.format(my_circle.area))
print('Circle circumference: {}'.format(my_circle.get_circumference()))