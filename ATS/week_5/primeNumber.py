
list_number = [1 for num in range(1,100)]
# print(list_number)

for key, value in enumerate(list_number):
    for j in range(2,key):
        if key % j == 0:
            list_number[key] = 0
            break
        elif key % j != 0:
            list_number[key] = 1
print(list_number)
