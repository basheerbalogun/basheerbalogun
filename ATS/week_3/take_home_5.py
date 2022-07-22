
def check_for_prime(number):
    
    print ("The Prime Numbers in the range are: ")  
    for number in range (2, 1000):  
        if number > 1:  
            for i in range (2, number):
                if (number % i) == 0:  
                    break  
            else:  
                print (number)

check_for_prime(20)

