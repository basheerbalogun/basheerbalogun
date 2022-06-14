perfect_num =int(input(": "))

aliquot_sum = 0

for i in range(1,perfect_num):
    if perfect_num % i == 0:
        aliquot_sum = aliquot_sum + i
if aliquot_sum == perfect_num:
    print(perfect_num," is perfec number")
else:
    print(perfect_num, "is not a perfect number")
