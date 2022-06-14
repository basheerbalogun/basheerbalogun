import string 

def upper_and_lower(word):
    lower_alpha=string.ascii_lowercase
    upper_alpha =string.ascii_uppercase
    char1 = 0
    char2= 0
    for char in word:
        if char in lower_alpha:
            char1 = char1 + 1
        
            
        else:
            char2 = char2 + 1
            

    
    print("lowercase : " , char1)
    print("uppercase : ", char2)

print(upper_and_lower(input(": ")))

