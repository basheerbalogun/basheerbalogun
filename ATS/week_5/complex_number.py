# realPart + imaginaryPart * i
class Complex:


    def __init__(self,real_part1 = 0.0,real_part2 = 0.0,imaginaryPart2 = 0.0 ,imaginaryPart1= 0.0) -> None:
        self.real_part1 = real_part1
        self.real_part2 = real_part2
        self.imaginaryPart1 = imaginaryPart1
        self.imaginaryPart2 = imaginaryPart2

    def add_two_complex_number(self):
        real=self.real_part1 + self.real_part2
        img = self.imaginaryPart1 + self.imaginaryPart2

        return f'{real  + img}'

    def subtracte_complex(self):
        
        real=self.real_part1 - self.real_part2
        img = self.imaginaryPart1 - self.imaginaryPart2

        return f'({real,img })' 

    def complex(self):
        return f'({self.real_part1},{self.imaginaryPart1}) ({self.real_part2},{self.imaginaryPart2})'

complex = Complex(4,3,1,6)
print(complex.add_two_complex_number())