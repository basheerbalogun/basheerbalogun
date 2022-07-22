import random

def password_generation():

    randpassword= '12345ADGGGRYUKJSHGceqy132526ikmbghjdiu67890@#$%^&*'
    your_password = random.sample(randpassword,8)

    #  for i in your_password:
    print("".join(your_password), end='')



password_generation()

