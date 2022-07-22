

class User:

    user_dict = {}    

    def __init__(self, name):
        self.name = name
    
    def new_user(self):
        self.firstname = User.get_firstname(self)
        self.lastname = User.get_lastname(self)
        self.username = User.get_username(self)
        self.password = User.get_password(self)
        self.email = User.get_email(self)
        self.address = User.get_address(self)

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





class Wallet:


    def __init__(self):
        pass


class Transaction:


    def __init__(self):
        pass