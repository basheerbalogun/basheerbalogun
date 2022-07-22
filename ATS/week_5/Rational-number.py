# Create a class called RationalNumber for performing arithmetic with fractions. Write a
# driver program to test your class
# Use integer variables to represent the data of the class the numerator and the denominator.
# Provide a constructor that enables an object of this class to be initialized when it is declared. The
# constructor should contain default values, in case no initializers are provided, and should store the
# fraction in reduced form (i.e., the fraction 
# would be stored in the object as 1 in the numerator and 2 in the denominator). Provide methods for
# each of the following:
# a) Adding two RationalNumbers. The result should be stored in reduced form.
# b) Subtracting two RationalNumbers. The result should be stored in reduced form.
# c) Multiplying two RationalNumbers. The result should be stored in reduced form.
# d) Dividing two RationalNumbers. The result should be stored in reduced form.
# e) Printing RationalNumbers in the form a/b, where a is the numerator and b is the
# denominator.
# f) Printing RationalNumbers in floating-point format


class RationalNumber:


    def __init__(self, numerator1 : int =1,numerator2 :int = 1 ,denominator1 : int =1,denominator2 : int=1 ):

        self.numerator1 = numerator1
        self.denominator1 = denominator1
        self.numerator2 = numerator2
        self.denominator2 = denominator2

    def check_number(self):
        if isinstance() > 0:
            #count out the floats
            return True
        raise Exception("Input number that is greater than 0")

    def get_find_lcm(self):
        if self.check_number():
            self.lcm = 0
            if self.denominator1 % self.denominator2 == 0:
                self.lcm = self.denominator1
            elif self.denominator2 % self.denominator1 == 0:
                self.lcm = self.denominator2
            else:
                self.lcm = self.denominator1 * self.denominator2
            return self.lcm
        else:
            self.get_find_lcm() 
    @staticmethod      
    def gcd(n, d):
            while d != 0:
                t = d
                d = n%d
                n = t
            return n

    @staticmethod
    def reducefract(n, d):
        RationalNumber.gcd(n,d)

        assert d!=0, "integer division by zero"
        assert isinstance(d, int), "must be int"
        assert isinstance(n, int), "must be int"
        greatest=RationalNumber.gcd(n,d)
        n/=greatest
        d/=greatest
        return int(n), int(d)
 

    def adding_two_rational_number(self) -> int:

        self.upper_value = self.numerator1 + self.numerator2
        self.lower_value = self.get_find_lcm()

        return self.reducefract(self.upper_value,self.lower_value)

        # return f'{self.upper_value} / {self.lower_value}'

    def  Subtracting_two_RationalNumbers(self) -> int:

        self.upper_value = self.numerator1 - self.numerator2
        self.lower_value = self.get_find_lcm()

        return f'{self.upper_value} / {self.lower_value}'

    def multiply_two_rational_number(self):

        self.upper_value = self.numerator1 * self.numerator2
        self.lower_value = self.get_find_lcm()
        return f'{self.upper_value} / {self.lower_value}'

    def  dividing_two_RationalNumbers(self):
        self.upper_value = self.numerator1 * self.denominator2
        self.lower_value = self.denominator2 * self.denominator1
        return f'{self.upper_value} / {self.lower_value}'

    def  printing_RationalNumbers(self):
        return f'{self.numerator1}/{self.denominator1},{self.numerator2}/{self.denominator2}'

    def rationalNumbers_in_floating_point(self):
        self.upper_value = self.numerator1 + self.numerator2
        self.lower_value = self.get_find_lcm()
        return f'{self.upper_value / self.lower_value}'

rational_number = RationalNumber(2,4,3,6)
print(rational_number.adding_two_rational_number())


    
