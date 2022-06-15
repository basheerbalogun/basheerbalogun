
number = int(input("Enter a binary number: "))

arr = []

while number > 0:
    arr = [number % 10] + arr
    number = int(number / 10)

print(arr)

accumulator = 0
multiply_by = 1
current_bin = len(arr) - 1
while current_bin >= 0:
    accumulator += arr[current_bin] * multiply_by
    current_bin -= 1
    multiply_by *= 2

print(accumulator)

