
from calendar import c


vowels = ['a','e','i','o','u']
ask = input(": ")
ask.split(",")

print("the first 10 letters of the is are : ",ask[0:10])
print("the last 10 letters of the is are : ",ask[10:20])

v=[]
c=[]
for char in ask.lower():
    if char in vowels:
        v.append(char)
    else:
        c.append(char)
print(v)
print(c)


