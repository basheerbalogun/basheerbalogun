
first_int = int(input("Enter the first number : "))
second_int = int(input("Enter the second number : "))
third_int = int(input("Enter the third number : "))

def factorization(a,b,c):
    product = a * c
    factors = []
    midd_term = []
    if product > 0:
        for i in range(-product,(product+1)):
            if i == 0:
                continue
            # if b%i == 0:
            factors.append(i)
                
        for x in factors:
            for j in range(1,factors):
                if x + x[j] == b and x * x == product:
                    midd_term.append(x)
    
    print(factors,midd_term)
    if a >= 1:
        print(f"The value of x are {-midd_term[0]} and {-midd_term[0]}")



if __name__ == "__main__":
    factorization(first_int,second_int,third_int)
