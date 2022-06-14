number=int(input("Enter a number: "))
if number > 0:
    print(f"{ number} is greater than 0")
if number < 0:
    print(f"{number} is less than 0")
if number == 0:
    print(f"{number} is greater than 0")

#formatting string
messa = input("Enter your name : ")
print("his name is {}".format(messa))

f_name = "bolu"
l_name = "ola"
print("his name is {1}{0}".format(f_name,l_name))
