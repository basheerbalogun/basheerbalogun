import csv


def collecting_data():
    global dict_data
    dict_data={}
    dict_data['firstname'] = input("Enetr you firstname : ")
    dict_data['lastname'] = input("Enter your lastname : ")
    dict_data['middlename'] = input("Enter your middlename : ")
    dict_data['age'] = int(input("Enter your age : "))
    dict_data['occupation']= input("What is your occupation : ")
    dict_data['d_of_birth'] = input("Enter your date of birth : ")
    dict_data['gender'] = input("Enter your gender : ")
    dict_data['marital_status'] = input("Are you married or single : ")
    dict_data['u_email']= input("Enter your email : ")

    with open("validation.csv", "w", newline='') as f:
        header = ['firstname','lastname','middlename','age','occupation','d_of_birth','gender','marital_status','u_email']
        handler= csv.DictWriter(f, fieldnames=header)
        handler.writeheader()
        handler.writerow(dict_data)


def read_file():
    with open("validation.csv","r") as f:
        handler = csv.reader(f)
    for row in handler:
        print(row)

def search():
    search_key = input("What is your first name : ")

    with open("validation.csv","r") as f:
        handler = csv.reader(f)
        for row in handler:
            if search_key.lower() == dict_data["firstname"].lower() or dict_data["lastname"].lower() or dict_data["middlename"].lower() or dict_data["u_email"].lower():
                print(row)

def select():
    print("Wecome to \nchoose 1 to read your file\nchoose 2 to search through your data")
    ask = int(input("Enter your choice : "))
    if ask == 1:
        read_file()
    elif ask == 2:
        collecting_data()
select()
