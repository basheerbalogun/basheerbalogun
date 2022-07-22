# (The Sieve of Eratosthenes) A prime integer is any integer greater than 1 that is evenly divisible 
# only by itself and 1. The Sieve of Eratosthenes is a method of finding prime numbers. It operates
# as follows:
# a) Create a list with all elements initialized to 1 (true). List elements with prime subscripts
# will remain 1. All other list elements will eventually be set to zero.
# b) Starting with list element 2, every time a list element is found whose value is 1, loop
# through the remainder of the list and set to zero every element whose subscript is a multiple of the subscript
#  for the element with value 1. For list subscript 2, all elements beyond 2 in the list 
# that are multiples of 2 will be set to zero (subscripts 4, 6, 8, 10, etc.);
# for list subscript 3, all elements beyond 3 in the list that are multiples of 3 will be set to
# zero (subscripts 6, 9, 12, 15, etc.); and so on.
# When this process is complete, the list elements that are still set to 1 indicate that the subscript is a
# prime number. These subscripts can then be printed. Write a program that uses a list of 1000 elements to determine 
# and print the prime numbers between 2 and 999. Ignore element 0 of the list.

sqr = []

for i in range(1,1001):
    print(sqr)
    sqr.append(i)
    i += 2


lower_value = 2  
upper_value = 999 

print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
    


