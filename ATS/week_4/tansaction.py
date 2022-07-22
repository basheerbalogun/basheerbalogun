


from ntpath import join
import random


class Wallet:

    user_arr = []

    def __init__(self, username, id, ) -> None:
        self.username = username
        self.id = id
    
    @staticmethod
    def balance(balance):
        return f'Your balance is : {balance}'
        

    def wallet_funding(self):
        self.name = User.get_username()
        self.pw = User.get_password()

        for data in Wallet.user_arr:
            try:
                if data['username'] == self.name and data["password"] == self.pw:
                    self.amount = int(input("How much are you funding your wallet with : "))
                    data["balance"] += self.amount
                    credit = 'your account has been credited by'
                    print(f'{credit} {self.amount}')

            except:
                return f'incorrect password'
        Wallet.wallet_funding()


class User(Wallet):


    def __init__(self, username, id) -> None:
        super().__init__(username, id)


        self.user_dict ={}

    def new_user(self):
        char = "ABCDEFGHIJKLMNOUPQRSTWXYZ"
        number = "1234567890"
        self.user_dict['firstname'] = User.get_firstname(self)
        self.user_dict['lastname'] = User.get_lastname(self)
        self.user_dict['username'] = User.get_username(self)
        self.user_dict['password'] = User.get_password(self)
        self.user_dict['email'] = User.get_email(self)
        self.user_dict['balance'] = 0

        ran= random.sample(number, 5) + random.sample(char,2)
        id="".join(ran)
        self.user_dict['id'] = id
        Wallet.user_arr.append(self.user_dict)

    def delete_user(self):
        self.password = User.get_password()
        for data in Wallet.user_arr:
            if data['password'] == self.password:
                del Wallet.user_arr[data]

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


class LoggingTransaction(Wallet):


    def __init__(self, f_name, l_name, id) -> None:
        super().__init__(f_name, l_name, id)

    def transaction_by_id(self):
        id = input("Enter your id : ")




user = User(input("Username : "), int(input("id : ")))
user.new_user()
wallet = Wallet('f',3)
print(wallet.user_arr)
