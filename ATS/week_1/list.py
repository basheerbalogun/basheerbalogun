'''squares = []
for x in range(1,11):
    squares.append(x)
print(squares)
'''

finishers=[]
for x in range(2):
    users=input("Enter your name:")
    finishers.append(users)

print(finishers)
print("you are welcome back")
ask=input("What is your name: ")
if ask.lower() in finishers:
    print("Welcome back {} again.".format(ask))
else:
    print("sorry ! your name can not be founded\nDo you want to register ?:")
    reg=input("Enter your name here : ")
    pas=input("Enter 6 digit password : ")
    if len(pas) > 6:
        print("You are npot allowed to enter number more than 6")
    else:
        finishers.append(pas)
    
    
    
