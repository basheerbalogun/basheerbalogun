import pandas as pd
from profile import Profile as user_profile

class SingleProfile(user_profile):


    def __init__(self, user_email, password):
        super().__init__()
        self.user_email = user_email
        self.__password = password
    

    def get_user_data(self):
        data = self.get_data()

        for profile in data:
            if profile['email'] == self.user_email:
                print(profile)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.confirm_email = input("Enter your email : ")
        if self.confirm_email != self.user_email:
            raise Exception("Incorrect email")
        else:
            self.__password = new_password

    def change_password(self):
        data = self.get_data()
        self.confirm_email = input("Enter your email : ")
        if self.confirm_email != self.user_email:
            raise Exception("Incorrect email")
        else:
            for index,profile in enumerate(data):
                profile['password'] = input("Enter your new password : ")

            df = pd.read_csv("sign_db.csv")
            df.loc[index, "password"] = profile["password"]
            df.to_csv("sign_db.csv", index=False)


single=SingleProfile('basher@gmail.com','basheer12')
print(single.change_password())

