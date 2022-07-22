# guessing game

import random

secret_number = random.randint(1,10)
count = 1
for quess_taken in range(0,5):
    take_your_guess = int(input("Take your guess : "))
    print(take_your_guess)

    if take_your_guess < secret_number:
        print("your quess is low")
    elif take_your_guess > secret_number:
        print("Your quess is high")
    elif take_your_guess == secret_number:
        break
    count +=1
    
if take_your_guess == secret_number:       
    print(f"You are done well you take my quess {count} ")

else:
    print(f"failed ! my quess is {secret_number}")

