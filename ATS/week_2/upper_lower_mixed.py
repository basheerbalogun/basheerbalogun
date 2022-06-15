
import string

def upper_lower_mixe(word):
    upp = string.ascii_uppercase
    low = string.ascii_lowercase
    mix = string.ascii_letters
    for char in word:
        if char in upp:
            return "word is in uppercase"
        elif char in low:
            return "word is in lowercase"
        elif char in upp + low:
            return "Mixed"

f= upper_lower_mixe(input(": "))
print(f)

