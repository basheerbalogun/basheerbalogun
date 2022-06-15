from pickle import TRUE
import string

def ispangram(word):
    alphabet=string.ascii_lowercase
    for char in alphabet:
        if char not in word:
            return False
    return True
    


ispangram(input(":"))
if ispangram == True:
    print("true")

else:
    print("false")