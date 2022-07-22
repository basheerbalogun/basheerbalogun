# write a program that asks for your username,firstname, lastname, password and password confirmartion
# and then saves them as a  text file with username

# def collecting_data():
#     forms = ["Enter your username","Enter your firstname","Enter your lastname","Enter your password"," onfirmation"]
#     data = {}
#     for d in forms:
#         ask = input(d)
#         data[d]=ask
#     with open(data["username"]+".txt", "w") as wf:
#         wf.write(f'{data}')
# pr = collecting_data()
# print(pr)




# def collecting_data():
#     username = input("Enter your username : ")
#     firstname = input("Enetr you firstname : ")
#     lastname = input("Enter your lastname : ")
#     password = input("Enter your password : ")
#     conf_password = input("confirm your password : ")


# def collecting_data():
#     forms = ["username","firstname","lastname","password","password confirmation"]
#     data = {}
#     for d in forms:
#         ask = input(d)
#         if ask[-1] == ask[3]:
#             data[d]=ask.upper()
#         else:
#             print("wrong password !")
#             collecting_data(d[4])

#     with open(data["username"]+".txt", "w") as wf:
#         wf.write(f'{data}')
    
    # strange = " "
    # for obj in data.values():
    #     strange = strange +" "+obj

    # with open(data["username"]+".txt", "w") as wf:
    #     wf.write(strange)
    # return strange

# pr = collecting_data()
# print(pr)

import csv
import email
from this import s

with open("info.csv","r") as f:
    handler = csv.reader(f)
    for row in handler:
        print(row)


# with open("info2.csv", "w") as f:
#     handler= csv.writer(f)
#     handler.writerow(["basheer","balogun","male"])



def collecting_data():
    firstname = input("Enetr you firstname : ")
    lastname = input("Enter your lastname : ")
    middlename = input("Enter your middlename : ")
    age = int(input("Enter your age : "))
    if type(age) != int:
        print("Enter an integer")
    else:
        occupation= input("What is your occupation : ")
        d_of_birth = input("Enter your date of birth : ")
        gender = input("Enter your gender : ")
        marital_status = input("Are you married or single : ")
        u_email= input("Enter your email : ")

    with open("validation.csv", "w") as f:
        handler= csv.writer(f)
        handler.writerows([firstname,lastname,middlename,age,occupation,d_of_birth,gender,marital_status,u_email])


def select():
    print("Wecome to \nchoose 1 to read your file\nchoose 2 to search through your data")
    ask = input("Enter your choice : ")
    if ask == 1:
        read_file()
    elif ask == 2:
        collecting_data()
select()
