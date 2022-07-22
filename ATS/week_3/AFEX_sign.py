import csv



header = ['username','email','firstname','lastname','password','phone_number','address','age','date_of_birth','gender']


def sign_in():
    read_csv()

    d ={}
    l = ['username','email','firstname','lastname','password','password again']

    for i in l:
        prompt = input(f"Enter your {i} :")
        d[i]=prompt

        if d["password"] != d["password again"]:
            return 'incorrect password',sign_in()
    print('sign up successfull')
    login()

    with open('AFEX_CSV.csv', mode='w+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)

        if len(read_csv()) == 0:
            writer.writeheader()
            writer.writerow(d)
        return writer.writerow(d)

        


def read_csv():
    with open("AFEX_CSV.csv", mode="r") as file:
        reader = csv.DictReader(file, fieldnames=header)
        return reader


def login():

    profile = read_csv()
    print('\n\t=============You are on login page===============')
    username = input("\n\tEnter your username : ")
    password = input("\n\tEnter your pasword : ")

    for record in profile:
        if record["username"] != username and record['password'] != password:
            return 'incorrrect username and password', login()

        else:
            print('login successfull ')
            edit_profile(username)
            return my_portfolio()



def my_portfolio():
    my_details = read_csv()
    for details in my_details:
        print("\n\t\t========MY PORTFOLIO=======")
        print

    






def home():
    print("\n\tWelcome to AFEX \n\tDo you have AFEX user account ?\n\if yes press 1 to login\n\t")
    prompt = input(": ")
    print('___________________')
    if prompt == "1":
        login()
    else:
        sign_in()

if __name__ == "__main__":
    home()