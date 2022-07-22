# write a class 
# Increase attendance
# update firstname and lastname
# list of fullnames in title case
# add profile
# return number of student
# remove profile
# return name of birth month
# group profile by birth month
# return list of initials
# calculate BMI
# return average age of the class
# return minimum age
# return maximum age
# calc birth year



class Student:



    profilelist ={"basheer@gmail.com":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
                "abdullahi@gmail.com":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "faith@gmail.com":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
                "ahmad@gmail.com": {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
                "toluwanimi@gmail.com":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
                "awwal@gmail.com": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
                "abdulwali@gmail.com": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
                "abraham@gmail.com": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "yusuff@gmail.com": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
                "adebusola@gmail.com": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
                "lukman@gmail.com": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}

    new_profilelist = {}
    
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        
        
        
    def increase_attendance(self, attendance):
        attendance = attendance['basheer@gmail.com']['attendance'] + 1
        print(f"your attendance has been increased by {attendance}")


    def update_first_and_lastname(self,email):

        prompt = input("Please enter your email to comfirm : ")

        if email[prompt]:
            f_name = input("Enter your new firstname : ")
            l_name = input("Enter your new lastname : ")
            # detail = email[prompt]

            # for v in detail.keys():
            email[prompt]["first_name"]= f_name
            email[prompt]["last_name"] = l_name
            print(f"Your full name now is :{f_name} {l_name}")
            print(email[prompt])




    def fullname_in_titlecase(self,email):
        prompt = input("Please enter your email to comfirm : ")
        if email[prompt]:
            fullname = email[prompt]["first_name"].title()+ ''+' '+ email[prompt]["last_name"].title()
            return fullname

    def add_new_profile(self,data):
        newbie_profile = {}
        em = input("Enter your email address : ")

        newbie_profile['first_name'] = input("Enter your new firstname : ")
        newbie_profile['last_name'] = input("Enter your new lastname : ")
        newbie_profile['attendance'] = int(input("Attendance : "))
        newbie_profile['height'] = int(input(" Your height : "))
        newbie_profile['weight'] = int(input(" Your weight : "))
        newbie_profile['age'] = int(input(" Your age : "))
        bday = {}
        bday['day']= int(input(" Day of your birthday : "))
        bday['month'] =input("Month of your birthday (Jan,Feb,March...) : ").title()

        newbie_profile["birthday"] = bday

        global new
        data[em] = newbie_profile
        new["1"] = data
        print(data)


        return newbie_profile

    def number_of_student(self,data,new):
        prompt = input("Please enter your email to comfirm : ")

        if data[prompt]:
            return len(new)

    def remove_profile(self,data):
        prompt = input("Please enter your email to comfirm : ")
        if data[prompt]:
            data.pop(prompt)
            return len(data)
        print(data)

    def name_of_birth_month(self,data):
        prompt = input("Please enter your email to comfirm : ")

        if data[prompt]:
            return data[prompt]["birthday"]["month"].title()

    def group_profile_by_birth_month(self,data):
        month=input("Enter the month of your birthday : ")
        same_birth=[]
        for i in data:
            if data[i]['birthday']['month']== month:
                same_birth.append(data[i])
        return same_birth

    def return_list_of_initials(self,data):
        for x in data:
            print(data[x]['first_name'][0] + data[x]["last_name"])[0]


    def calculate_BMI(self,data):
        hgt = int(input("Enter your heiht: "))
        wgt= int(input("Enter your weight : "))
        for i in data:
            if data[i]["height"]== hgt and data[i]["weight"] == wgt:
                bmi = wgt / (hgt**2)
                print("your bmi is {}".format(bmi))

    def average_age(self,data):
        total = 0
        for i in data:
            total = total + data[i]["age"]
        average = total/ len(i)
        return f"the average age is {average}"

    def max_age(self,data):
        emp_list = []

        for i in data:
            emp_list.append(i["age"])
        sorted_list = sorted(emp_list)[-1]

        return f"Maximun age is {sorted_list}"

    def minimum_age(self,data):
        emp_list = []
        for i in data:
            emp_list.append(i["age"])

        sorted_list = sorted(emp_list)[0]
        print(f'minimum age is {sorted_list}')

    def birth_year(data,year):

        current_year = 2022
        for i in data:
            if data[i]["age"]==year:
                current_year = current_year - year
            print(f"You were born in {current_year}")




def main():

    p = Student()
    data = p.profilelist

    n = Student()
    new = n.new_profilelist
    new["1"] = data

    print("""
    Choose your option
    1)  To increment your attendance
    2)  update firstname and lastname
    3)  list of fullnames in title case
    4)  add profile
    5)  return number of student
    6)  remove profile
    7)  return name of birth month
    8)  group profile by birth month
    9)  list of initial profile names
    10) calculate BMI
    11) calculate average age
    12) minimum age
    13) minimum_age
    14) calc birth year
    """)
    ask = int(input("option : "))
    if ask == 1:
    #calling increase method to increase attendance value by 1
        print(p.increase_attendance(data))
    elif ask == 2:
        print(p.update_first_and_lastname(data))
    elif ask == 3:
        full=p.fullname_in_titlecase(data)
        print(full)
    elif ask == 4:
        newprofile = p.add_new_profile(data)
        print(newprofile)
    elif ask == 5 :
        print(p.number_of_student(data,new))
    elif ask == 6:
        print(p.remove_profile(data))
    elif ask == 7:
        print(p.name_of_birth_month(data))
    elif ask == 8:
         print(p.group_profile_by_birth_month(data))
    elif ask == 9:
        print(p.return_list_of_initials(data))
    elif ask == 10:
        print(p.calculate_BMI(data))
    elif ask == 11:
        print(p.average_age(data))
    elif ask == 12:
        print(p.max_age(data))
    elif ask == 13:
        print(p.minimum_age())
    elif ask == 14:
        print(p.birth_year(data))

if __name__ == "__main__":
    main()
