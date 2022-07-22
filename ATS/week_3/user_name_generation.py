
import random

# programe that takes in 
def username_generation(firstname,lastname):
    fname =[]
    sname = list(lastname)
    # firstname = 'Basheer'
    # firstname= 'Balogun'
    for first in firstname:
        fname.append(first)
    username = fname[2:2] + sname
    user = random.sample(username,7)

    return ''.join(user)
f_name = input("enter your firstname : ")
l_name = input("Enter your lastname : ")
print(username_generation(f_name,l_name))