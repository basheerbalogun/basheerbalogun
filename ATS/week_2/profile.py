

profilelist ={"n_1":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
             "n_2":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "n_3":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
               'n_4': {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
              "n_5":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
               "n_6": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
               "n_7": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
               "n_8": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
               "n_9": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
               "n_10": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
               "n_11": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}



def inc_att(data, firstname, increment = 1):
   for x in data:
      if data[x]["first_name"] == firstname:
         data[x]["attendance"] += increment
         return data
# print(inc_att(profilelist, input("Enter your first name: "),))



#update profile first name and last name
def update_fullname(profile, your_age,f_name,l_name:str):
   for i in profile:
      if profile[i]["age"] == your_age :
         profile[i]["first_name"] = f_name
         profile[i]["last_name"] = l_name
         return profile
# up=update_fullname(profilelist, int(input("Enter your age: ")), input("Enter Your first name : "), input("Enter Your last name : "))
# print(up)


# function to return full names 
def f_and_l_title(data):

   fullname = []
   for x in data:
      fullname.append(data[x]['first_name'].title() +" "+ data[x]["last_name"].title())
      #print()

   return fullname
# print(f_and_l_title(profilelist))
      





def increament_attendance(data):
   
   dict_2={}
   f_name = input("Enter your first name : ")
   l_name = input("Enter your last name : ")
   att = int(input("Attendance : "))
   h = int(input(" Your height : "))
   w = int(input(" Your weight : "))
   a = int(input(" Your age : "))
   bday = {}
   day = int(input(" Day of your birthday : "))
   month =input("Month of your birthday : ")
   bday["day"]=day
   bday['month']=month
   new_dict ={}
   new_dict["first_name"]=f_name
   new_dict["last_name"]=l_name
   new_dict['attendance']= att
   new_dict["height"]=h
   new_dict["weight"]=w
   new_dict["age"]=a
   new_dict["birthday"]=bday
   data["n_12"]=dict_2
   return data
# inc=increament_attendance(profilelist)
# print(inc)


# A function that returns the number of people in class
def number_of_people(data):
      return len(data)
# print(number_of_people(profilelist))



# to remove a profile from class
def remove_profile(data,f_name):
   for x in data:
      if data[x]["first_name"]== f_name:
         del data[x]
      return data

# print(remove_profile(profilelist, "Basheer" ))

# group all profiles that have the same month name 
def group_profile_by_month(data, month):

   same_birth=[]
   for i in data:
      if data[i]['birthday']['month']==month:
         same_birth.append(data[i])
   return same_birth

group = group_profile_by_month(profilelist,input("Select month : "))
print(group)


def initial(data):
   init = []
   for x in data:
      print(data[x]['first_name'][0] + (data[x]["last_name"])[0])

# initial(profilelist)

def profile_BMI(data,hgt, wgt):
   for i in data:
      if data[i]["height"]== hgt and data[i]["weight"] == wgt:
         bmi = wgt / (hgt**2)
   print("your bmi is {}".format(bmi))
profile_BMI(profilelist,int(input("Enter your heiht: ")), int(input("Enter your weight : ")))

# To calculate the average age
def average_age(data):
   total = 0
   for i in data:
      total = total + data[i]["age"]
   average = total/ len(i)
   print("the average age is ", average)

print(average_age(profilelist))


def max_age(data): 
   emp_list = []
   for i in data:
      emp_list.append(i["age"])

   sorted_list = sorted(emp_list)[-1]
   print(f"Maximun age is {sorted_list}")
max_age(profilelist)

def minimum_age(data):
   emp_list = []
   for i in data:
      emp_list.append(i["age"])

   sorted_list = sorted(emp_list)[0]
   print(f'minimum age is {sorted_list}')

# minimum_age(profilelist)

def age(data,year):

   current_year = 2022
   for i in data:
      if data[i]["age"]==year:
         current_year = current_year - year
      print(f"You were born in {current_year}")

print(age(profilelist,int(input("Enter your age : "))))


