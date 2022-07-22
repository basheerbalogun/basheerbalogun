# Create a user class , wallet, transaction class
# Each of the other classes should inherit from the User class
# Update your code such that some operations can be performed on the user class such as
# 1.Creating a user
# 2.Deleting
# 3.Funding the wallet
# 4.Logging transactions

import csv
import time, random
from datetime import datetime

import pandas as pd


class User:
    header = ['firstname', 'lastname', 'username', 'password', 'email','user_id', 'balance']
    history_header = ['ID','SENDER','CREDITED','TIME']

    def __init__(self):
        pass

    def new_user(self):
        char = "ABCDEFGHIJKLMNOUPQRSTWXYZ"
        number = "1234567890"
        f_name = User.get_firstname(self)
        l_name = User.get_lastname(self)
        u_name = User.get_username(self)
        p_word = User.get_password(self)
        e_mail = User.get_email(self)
        ran = random.sample(number, 5) + random.sample(char, 2)
        id = "".join(ran)
        my_balance = 0

        User.save_data(self, firstname=f_name, lastname=l_name, username=u_name, password=p_word, email=e_mail,user_id = id,
                       balance=my_balance)
        LoggingTransaction.perform_tansaction(self)

    def get_data(self):
        with open("user.csv", "r") as file:
            writer = csv.DictReader(file)
            return list(writer)

    def save_data(self, **kwargs):
        with open("user.csv", "a+", newline="\n") as f:
            handler = csv.DictWriter(f, fieldnames=User.header)
            handler.writerow(kwargs)

    def get_username(self):
        return input("Enter your user name : ")

    def get_password(self):
        return input("Enter your password : ")

    def get_firstname(self):
        return input("Enter your first name : ")

    def get_lastname(self):
        return input("Enter your last name : ")

    def get_email(self):
        return input("Enter your email address : ")

    def account_deleting(self):
        data = User.get_data(self)
        username = input("Enter your username : ")
        for k, i in enumerate(data):
            if i["username"] == username:
                i["firstname"] = "#"
                i["lastname"] = "#"
                i["username"] = "#"
                i["password"] = "#"
                i["email"] = "#"
                i["user_id"] = "#"
                i["balance"] = "#"

            df = pd.read_csv("sign_db.csv")
            df.loc[k, "firstname"] = i["firstname"]
            df.loc[k, "lastname"] = i["lastname"]
            df.loc[k, "username"] = i["username"]
            df.loc[k, "password"] = i["password"]
            df.loc[k, "email"] = i["email"]
            df.loc[k, "user_id"] = i["user_id"]
            df.loc[k, "balance"] = i["balance"]
            df.to_csv("sign_db.csv", index=False)



class Wallet(User):

    def __init__(self):
        super().__init__()

    def check_balance(self):
        data = user.get_data()
        username = user.get_username()
        password = user.get_password()

        for profile in data:
            if profile['username'] == username and profile['password'] == password:
                print('{} your account balance is : {}'.format(profile['firstname'], profile['balance']))

            print(f'{profile["firstname"]} you entered invalid credential')

        LoggingTransaction.perform_tansaction(self)

    @property
    def wallet_funding(self):
        data = user.get_data()
        try:
            password = user.get_password()
            for i, profile in enumerate(data):

                if profile['password'] == password:
                        amount = float(input("Enter amount to fund your wallet with : "))

                        # add user amount to the current one in csv
                        df = pd.read_csv("user.csv")
                        df.loc[i, 'balance'] = float(profile['balance']) + amount
                        df.to_csv("user.csv", index=False)

                        LoggingTransaction.transaction_history(self,ID=profile['user_id'],SENDER=profile['username'],CREDIT=amount,TIME=datetime.now())
        except :
            print("Error,Make sure you input correct password\ntry again.")
            w.wallet_funding()


    def transfer(self):
        pass



class LoggingTransaction(User):

    def __init__(self):
        super().__init__()
        # self.username = self.get_username()

    def transaction_history(self, **kwargs):
        with open("user_history_db.csv", "a+") as f:
            write = csv.DictWriter(f, fieldnames=User.history_header)
            write.writeheader()
            write.writerow(kwargs)

    def perform_tansaction(self) -> object:
        
        try:
            print('''
            Choose your option
    
            1)To create new user
            2)To check your balance
            3)To delete your account
            4)To fund your wallet
            5)To transfer fund
            
            ''')
    
            prompt = int(input("Which transaction will you like to do : "))
    
            if prompt == 1:
                time.sleep(1)
                user.new_user()
    
            elif prompt == 2:
                time.sleep(1)
                w.check_balance()
    
            elif prompt == 3:
                time.sleep(1)
                user.account_deleting()
    
            elif prompt == 4:
                time.sleep(1)
                w.wallet_funding

            elif prompt== 5:
                time.sleep(1)

                
        except:
            print('Please,select from option above')
        
        transaction.perform_tansaction()
        


if __name__ == "__main__":
    user = User()
    w = Wallet()
    transaction = LoggingTransaction()
    transaction.perform_tansaction()

