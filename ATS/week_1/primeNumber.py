
def prime_number(number):
    for i in range(2,number):
        if number % i == 0:
            print(number,"it is not a prime number")
            break
    else:
        print("it is a prime number")
prime_number(int(input(": ")))