import csv, sys
import pandas as pd


class Profile:
    
    header = ['username' ,'firstname' ,'middlename' ,'lastname' ,'email' ,'password','user_id','phonenumber','address']

    def __init__(self):
        pass
    def profile_editting(self):
        data = self.get_data()
        user = input("enter your username to proceed")
        password = self.get_password()

        for k ,i in enumerate(data):
            if i["username"] == user and i["password"] == password:
                i["password"] = input("enter your password : ")
                i["phonenumber"] = input("Enter your phone number : ")
                i["email"] = input("Enter your email : ")
                i["address"] = input("Enter your address : ")

            df = pd.read_csv("sign_db.csv")
            df.loc[k, "password"] = i["password"]
            df.loc[k, "phonenumber"] = i["phonenumber"]
            df.loc[k, "email"] = i["email"]
            df.loc[k, "address"] = i["address"]
            df.to_csv("sign_db.csv", index=False)

        print("Edit successful")

    def sign_up(self):
        self.username = self.get_username()
        self.firstname = self.get_firstname()
        self.middlename = self.get_middlename()
        self.lastname = self.get_lastname()
        self.password = self.get_password()
        self.confirm_password = self.get_confirm_password()

        if not self.username.isalnum():
            return f'username is incorrect'


        Profiles.save_data(username = self.username, firstname = self.firstname ,middlename = self.middlename
                           ,lastname = self.lastname ,password = self.password)

    def sign_in(self):
        data = Profiles.get_data(self)
        user =Profiles.get_username(self)
        pass_word = Profiles.get_password(self)
        for profile in data:
            if profile["username"] == user and profile['password'] == pass_word:
                print("Login successful ")
                return self.homepage()

        print("Invalid login credentials ")

    def homepage(self):
        print('''
        1) Edit your profile 
        2) Log out
        ''')
        ask = int(input("What will you like to do ? : "))
        if ask == 1:
            self.profile_editting()
        else:
            sys.exit()

    def get_username(self):
        return input("Enter your username : ")

    def get_firstname(self):
        return input("Enter your firstname : ")

    def get_middlename(self):
        return input("Enter your middlename : ")

    def get_lastname(self):
        return input("Enter your lastname : ")

    def get_password(self):
        return input("Enter your password : ")

    def get_confirm_password(self):
        return input("Please confirm your password : ")

    def get_email(self):
        return input("Enter your email address : ")

    def get_phone_number(self):
        return input("Enter your phone number : ")

    def get_address(self):
        return input("Enter your home address : ")

    def get_data(self):
        with open("sign_db.csv", 'r') as f:
            handler = csv.DictReader(f)
            return list(handler)

    def save_data(**kwargs):
        with open("sign_db.csv", 'w', newline="\n") as f:
            writer = csv.DictWriter(f, fieldnames=Profiles.header)
            writer.writeheader()
            writer.writerow(kwargs)

    def main(self):

        print('''
        1) To sign in
        2) To sign up
        
        ''')
        prompt = input("Choose your option : ")
        if prompt == "1":
            Profiles.sign_in(self)
        elif prompt == "2":
            Profiles.sign_up(self)
        else:
            sys.exit()




