# 1 - Create a Computation class with a default constructor (without parameters)
#  allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

from cgi import test


class Computation:


    def __init__(self):
        pass

    def factor(self, number):
        if number == 1:
            return 1
        else:
            return number * self.factor(number - 1)

    def sum(self, n):
        to_sum = 0
        for i in range(0,n + 1):
            to_sum += i
        return to_sum

    def test_prime(self, number):
        if number <= 1:
            raise Exception("Input number from 1 upward")
        
        for num in range(2,number):
            if number % num == 0:
                return f'{number} is not a prime number'
        return True

    def test_primes(self, number:int):

        number_to_list = []
        for j in range(1,number):
            number_to_list.append(j)
        # print(number_to_list)
        prime = []
        for y in number_to_list:
            counter = 0
            for x in range(1,y):
                if y % x == 0:
                    counter += 1
            if counter == 1:
                prime.append(y)
        
        print(prime)

    def table_mult(self, number):
        counter = 1
        multiplied_number = []
        while counter <= 12:
            num = number * counter
            multiplied_number.append(num)
            counter += 1
        print(*multiplied_number)

    def all_tables_mult(self, number):

        for i in range(1, number + 1):
            print("Multiplication table", i)
            counter = 1
            multiplied_number = []
            while counter <= 12:
                num = i * counter
                multiplied_number.append(num)
                counter += 1
            print(*multiplied_number)

    @staticmethod
    def list_div(number):
        Ldiv =[]
        for div in range(1,number + 1):
            if number % div == 0:
                Ldiv.append(div)
        return Ldiv

    def list_div_prime(self):

        list_prime_div = []
        data = self.list_div(9)
        for i in data:
            counter = 0
            for j in range(1,i):
                if i % j == 0:
                    counter += 1
            if counter == 1:
                list_prime_div.append(i)
        return list_prime_div
            

compute = Computation()
print(compute.test_primes(11))