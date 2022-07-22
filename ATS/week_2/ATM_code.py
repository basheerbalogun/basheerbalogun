
import time,sys,random


balance = 20000
string_num = "123445455678909754739210632468"
otp="".join(random.sample(string_num,4))
acc ="".join(random.sample(string_num,12))

def homepage(options="welcome"):
    global user_pin
    opt = 'Choose your option:\n\t1. Check Balance\n\t2. Transfer\n\t3. Buy Airtime\n\t4. Buy Data\n\t5. Generate OTP\n\t''6. Open Account'
    opti = "\n\nChoose your option|\n__________________________ : "
    option=opt + opti
    options = int(input(option))
    if options == "(q)uit":
        sys.exit()
               
    elif options == 1:
        check_balance()
    elif options ==2:
        transfer()
    elif options==3:
        buy_airtime()
    elif options == 4:
        buy_data()
    elif options == 5:
        generate_otp()
    elif options == 6 :
        open_account()
    else:
        print("You entered a wrong " )
        homepage()


def check_balance():
    digit = int(input("\n\tEnter your 4-digit pin\n\t____________________________"))
    if type(digit) == int and digit == user_pin:
        print('wait,while processing your request...')
        time.sleep(3)
        print('Your current balance is : {}\n\tThanks for banking with us.'.format(balance))
        take_decision()
    else:
        print(f'incorrect pin !')
        check_balance()
        

def transfer():
    global balance
    select = int(input("Enter account number of the res \n\t: _____________________"))
    amount = int(input("Amount to transfer\n\t:_____________________"))
    bank = input("\n\tEnter bank name : ")
    if amount > balance:
        print("Insuffient found !")
        transfer()
    else:
        pi = int(input("Enter your pin to confirm the transaction\n\t:_____________________"))
        print("transfer in progress...")
        time.sleep(2)
        balance -= amount
        if pi == user_pin:
            print("\n\tTransfer successful.")
            debit_alart = f'Dear {u_name} amount of {amount} \nwas Transfer to this account number'
            debit_alart += f'{select} {bank}\n your remaining balance is: {balance}\n\n\t{time.ctime()}'
            print(debit_alart)
        
        elif not pi:
            print("you entered an incorrect pin !,forgotten your pin or you want to try again ?")
            print("\n\tTo try again press 1\n\tTo reset your pin press 2")
            take_step = int(input(":__________________"))
            if take_step == 1:
                transfer()
            ussd()
    homepage()



def buy_airtime(user_pin):
    buy_card = int(input("Buy for yourself or others:\n\t1) Press 1 for yourself\n\t2) Press 2 for others\n\t3) Back"))
    if buy_card == 1:
        price=print(input("Enter amount  : "))
        your_pin =int(input("Enter your 4-digit pin to confirm the transaction: "))
        if your_pin == user_pin and price < balance: 
            print("Please wait...")
            time.sleep(3)
            print("Airtime has been sent.")
            balance = balance - price
            debit_alart = f'Dear {u_name} you purchase {price} airtime\n'
            debit_alart += f'\n your balance is : {balance}\n\n\t{time.ctime()}'
            print(debit_alart)
            take_decision()
        else:
            print("you entered incorrect pin : ")
            buy_airtime()

    elif buy_card == 2:
        phone = int(input("Enter the phone number to buy airtime for : "))
        amount = int(input("Enter amount : "))
        pin = int(input("Enter your 4-digit pin to confirm the transaction : "))
        if pin == user_pin and amount < balance:
            print("Transaction in progress...")
            time.sleep(3)
            balance -= amount
            print(f"The {amount} of airtime has been purchased for {phone} \n your balance is : {balance}\n\n\t{time.ctime()}")
        
        else: 
            print("you either entered incorrect pin or insufficient found ")
            buy_airtime()
    
    homepage()


#      
def buy_data():
    buy_da = int(input("Buy for yourself or others:\n\t1) Press 1 for yourself\n\t2) Press 2 for others\n\t3) Back"))
    if buy_da == 1:
        price=print(input("Enter amount  : "))
        mb_gb = input("In Gb or Mb : ")
        your_pin =int(input("Enter your 4-digit pin to confirm the transaction: "))
        if your_pin == user_pin and price < balance: 
            print("Please wait...")
            time.sleep(3)
            print("Data has been sent.")
            balance = balance - price
            debit_alart = f'Dear {u_name} you purchase {price}{mb_gb} data\n'
            debit_alart += f'\n your balance is : {balance}\n\n\t{time.ctime()}'
            print(debit_alart)
            take_decision()
        else:
            print("you entered incorrect pin : ")
            buy_airtime()

    elif buy_da == 2:
        phone = phone
        amount = amount
        pin = pin
        if pin == user_pin and amount < balance:
            print("Transaction in progress...")
            time.sleep(3)
            balance -= amount
            print(f"The {amount} of data has been purchased for {phone} \n your balance is : {balance}\n\n\t{time.ctime()}")
        
        else: 
            print("you either entered incorrect pin or insufficient found ")
            buy_airtime()
    
    homepage()


def generate_otp():
    print('your one time password is : ',otp)
    take_decision()


# This function generates account number after signing up
def open_account():
    global acc
    form_rows = ["First Name: ","Middle Name: ","Last Name: ","Phone Number: ",
        "Address: ","Account status: ","Land Mark: ","Email"]
    user =""
    form_dic = {}
    for form in form_rows:
        user = input("\n\t"form)
        form_dic[form]=user
    
    for k,v in form_rows.items():
        print("\n\tDear Mr {}, {} OTP has been sent to your {}, Kindly confirm it"
        "to active your account".format(k["First Name: "], otp, v.get("Email", "email")))
        confirm = int(input("\n\tEnter OTP sent to you here: "))
        if confirm == otp:
            print("Authenticating...")
            time.sleep(4)
            print("\n\tCongratulations,Welcome to First Bank.\n\tAccount Number: {}\n\tAccount Name: {}"
            "kindly found your account before 24-hours".format(acc, k["Last Name: "] +" "+k["First Name: "]+" "+k["Middle Name: "]))
            take_decision()
            time.sleep(2)

        else:
            print("Authenticating...")
            time.sleep(3)
            print("Authentication fails.")
            open_account()


# Take decision after every transaction
def take_decision():
    prompt =input("Do you want to perform another transaction ? if yes press 'y' if no press 'n'\n\tYes\n\tNo\n\t : ")
    print("\n\t___________________________")
    if prompt.lower() == 'y':
        homepage()
    else:
        print("Goodbye, have anice day.")
        sys.exit()



# Entery section where you can enter first bank ussd code (*894#) 
# and generate your 4-digt pin
def ussd(name,code):
    print(f"\t {name.title()} Welcome To First Bank")
    global u_name
    global user_pin
    user_pin = int(input("Enter any 4_digit pin to be your password: "))
    if code == "*894#":
        homepage()
    else:
        ussd()

u_name =input("\nEnter your First name here: ")
f_ussd = input("Enter our ussd code here: ")
ussd(u_name ,f_ussd)



