# basic calculator


def add():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number : "))
    return x+y

def subtract():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number : "))
    if x < y:
        return y - x
    elif x > y:
        return x-y
    else:
        return x -y or y-x

def multiply():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number : "))
    return x * y

def division():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number : "))

    if x < 1 or y < 1:
        return 'Enter number from one upwards', division()
    
    else:
        return x/y

def operators():

    print(r"""
    1 division 
    2 multiplication
    3 addition
    4 subtraction
     """)

    prompt = int(input("what operation will you like to do :"))
    print(prompt)
    if prompt == 1:
        division()
    elif prompt == 2:
        multiply()
    elif prompt == 3:
        add()
    elif prompt == 4:
        subtract()

if __name__ == "__main__":
    operators()
