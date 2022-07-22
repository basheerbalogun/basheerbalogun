# For your task today, duplicate your program from yesterday into another file and modify it as thus:
# 1. After successful signup, it should prompt the user to signin.
# 2. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
# 3. Edit profile should ask for more information like phone_number (required), address (optional), date of birth
#  (optional) and gender (compulsory) 
# Happy coding!!!

import csv

def sign_up():
    global data
    data={}
    data["username"] = input("Enter your user name : ")
    data['firstname'] = input("Enetr you firstname : ")
    data['lastname'] = input("Enter your lastname : ")
    password = input("Enter your password (with characters not less than 8) : ")
    password_2 = input("Please confirm your password : ")
    data["password"] = password
    data['confirm_password']= password_2

    if len(password) != 8:
        print("your password is strong!")
        if password_2 == password:
            print("Your password is correct")
            print("Succesfull!")
            
            print("you will be redirected to log in page ...")
            log_in()
        else:
            print("your paasword is in correct")
    elif len(password) < 8:
        print("your password is week, sorry enter the strong one to be secured")
    global row
    with open('sign_in.csv', "a") as f:
        header=['username','firstname','lastname','password','confirm_password']
        handler = csv.DictWriter(f, fieldnames=header)
        handler.writeheader()
        handler.writerow(data)

        print("Now you can log in")
        log_in()


def log_in():
    user = input("Enter your username : ")
    password = input("Enter your password here : ")
    if user == data["username"] and data['password'] == password:
        print("ling in succesfull")
    else:
        print("wrong password ! , try again")
        log_in()


def home():
    print(f"\n\tWelcome to AFEX ".center(10,"="))
    print("Do you have AFEX user account? if yes prss 1 to login else press 2 to sign up ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        log_in()
    elif choice == 2:
        sign_up()

home()

