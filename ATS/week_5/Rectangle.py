# Create a class Rectangle. The class has attributes __length and __width, each of
# which defaults to 1. It has methods that calculate the perimeter and the area of the rectangle. It
# has set and get methods for both __length and __width. The set methods should verify that
# __length and __width are each floating-point numbers larger than 0.0 and less than 20.0. Write
# a driver program to test the class.

from decimal import Decimal

class Rectangle:

    def __init__(self, length = 1, width = 1):

        self.__length = length
        self.__width =  width

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):

        if Decimal(value > '0.0' and value < '20.0') :
            raise Exception(" Value must greater than 0.0 and less than 20.0 ")
        self.__length = value


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if Decimal(value > '0.0' and value < '20.0') :
            raise Exception(" Value must greater than 0.0 and less than 20.0 ")
            
        self.__width = value

    def get_area(self):

        return f'{self.__length * self.__width}'

    def get_perimeter(self):

        return f'{ 2 * (self.__length * self.__width)}'


rect = Rectangle(6.2,5.4)
print(rect.get_area())
print(rect.get_perimeter())