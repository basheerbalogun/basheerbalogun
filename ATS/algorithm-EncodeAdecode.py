from email.headerregistry import BaseHeader
import string

def encode(data:str):
    digit=string.digits
    schars=string.punctuation
    alpha_lower=string.ascii_lowercase
    alpha_upper=string.ascii_uppercase
    rev_alpha_lower=alpha_lower[::-1]
    vowels=['a','e','i','o','u']
    vowels_map=['#','$','%','&','*']

    enc=[]

    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s.lower())])
        elif s in schars:
            enc.append('|'+ s)
        elif s in alpha_lower + alpha_upper:
            enc.append(s.swapcase())
        elif s in digit:
            enc.append('^'+ rev_alpha_lower[digit.index(s)])
    
    print(''.join(enc))

    
encode(input("Enter a string: "))

def decode(dat:str):
    digit=string.digits
    schars=string.punctuation
    alpha_lower=string.ascii_lowercase
    alpha_upper=string.ascii_uppercase
    rev_alpha_lower=alpha_lower[::-1]
    vowels=['a','e','i','o','u']
    vowels_map=['#','$','%','&','*']
    data = list(dat)
    strange = []

    for s in data:
        if s.lower() in vowels_map:
            strange.append(vowels[vowels_map.index(s.lower())])
        
        elif s == '|':
            strange.append(data[data.index(s) + 1])
            data.pop(data.index(s) + 1)
        elif s in alpha_lower + alpha_upper:
            strange.append(s.swapcase())
    print(''.join(strange))  
decode(input('Decode : ')) 

















