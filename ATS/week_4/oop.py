# create a class for all 
# Circle
# Triangle(base and height as )
# Rectangle
# 

from math import pi


class Triangle:


    def __init__(self , base, height,third_side):
        self.base = base
        self.height = height
        self.third_side = third_side
        

    def get_area(self):
        return f'{0.5 * (self.base * self.height)}'

    def get_perimeter(self):
        return f'{self.base + self.height + self.third_side}'

class Rectangle():

    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def get_area(self):

        return f'{self.length * self.breadth}'

    def get_parimeter(self):

        return f'{2 * (self.lenght* self.breadth)}'

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return f'{(pi * (self.radius ** 2))}'

    def get_perimeter(self):
        return f'{(2 * (pi * 2))}'


class Rhombus:

    def __init__(self,side, height):
        self.side = side 
        self.heigth = height

    def get_area(self):
        return f'{0.5 *(self.base * self.heigth)}'

    def get_parimeter(self):
        return f"{4 * (self.side)}"
        

c= Circle(3)
print(c.get_area()) 
print(c.get_perimeter())

t = Triangle(3,34,21)
print(t.get_area())
print(t.get_perimeter())