# The world of shapes is much richer than the shapes included in the inheritance hierarchy of Fig. 9.3. 
# Write down all the shapes you can think of—both two-di- mensional and 
# three-dimensional—and form them into a more complete Shape hierarchy with as many levels as possible.
#  Your hierarchy should have class Shape at the top. Classes TwoDimension- alShape and ThreeDimensionalShape should extend Shape. 
#  Add additional subclasses,
#  such as Quad- rilateral and Sphere, at their correct locations in the hierarchy as necessary.
from cmath import sqrt
from math import pi

class Shape:

    def __init__(self) -> None:
        pass

class TwoDimentionalShape(Shape):

    def __init__(self ,width, height,third_side):
        super().__init__()
        self.third_side = third_side
        self.height = height
        self.width = width

class Triangle(TwoDimentionalShape):


    def __init__(self,width,height,third_side) -> None:
        super().__init__(width, height, third_side)   

    def get_area(self):
        return f'{0.5 * (self.width * self.height)}'

    def get_perimeter(self):
        return f'{self.width + self.height + self.third_side}'

class Sqaure(TwoDimentionalShape):


    def __init__(self, breadth, length):
        super().__init__()
        self.breadth = breadth
        self.length = length

    def get_area(self):

        return f'{self.length * self.breadth}'

    def get_parimeter(self):

        return f'{4 * (self.lenght* self.breadth)}'

class Circle(TwoDimentionalShape):


    def __init__(self,width, height,radius):
        super().__init__(width, height)
        self.radius = radius

    def get_area(self):
        return f'{(pi * (self.radius ** 2))}'

    def get_perimeter(self):
        return f'{(2 * (pi * 2))}'


class ThreeDimentionalShape(Shape):


    def __init__(self,width, height):
        super().__init__(width,height)
        
class Sphere(ThreeDimentionalShape):


    def __init__(self,width,height, radius):
        super().__init__(width,height)
        self.radius = radius

    def get_area(self):
        return f'{4 * pi * (self.radius)**2 }'

    def get_volume(self):
        return f"{ 4/3 * pi * (self.radius)**3}"

class Cupe(ThreeDimentionalShape):


    def __init__(self, width, height, side):
        super().__init__(width, height)
        self.side = side

    def get_area(self):
        return f'({4 * (self.side)**2})'

    def get_volume(self):
        return f"{(self.side)**3}"

class Tetrahedron(ThreeDimentionalShape):

    
    def __init__(self, width, height, side):
        super().__init__(width, height)
        self.side = side

    def get_area(self):
        return f'{sqrt(self.side)**2}'

    def get_volume(self):
        return f"{self.side ** 3/ 6(sqrt(2))}"
        

cupe =Cupe(3,4,2)
print(cupe.get_volume())