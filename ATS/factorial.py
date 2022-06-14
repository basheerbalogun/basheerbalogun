
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# num = int(input('Enter a digit: '))
# print(factorial(num))


#factorial without using recursion

from math import prod


def factorial(num):
    a=list()
    for i in range(1,num+1):
        a.append(i)
        p =prod(a)
        print(p)
factorial(5)



