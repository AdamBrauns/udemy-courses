from math import pi

##############################################
# Problem 1
##############################################

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print("Line distance: {}".format(li.distance()))
print("Line slope: {}".format(li.slope()))

##############################################
# Problem 2
##############################################

class Cynlinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return pi * (self.radius ** 2) * self.height

    def surface_area(self):
        top = pi * (self.radius ** 2)
        return (2 * pi * self.radius * self.height) + (2 * top)

c = Cynlinder(2,3)
print("Cynlinder volume: {}".format(c.volume()))
print("Cynlinder surface area: {}".format(c.surface_area()))