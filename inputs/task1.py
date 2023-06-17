import random

random_number = random.randint(1, 11)
user_guess = int(input("Please, input your guess between 1 and 10: "))

if random_number == user_guess:
    print("Your guess is correct :)")
else:
    print("You are incorrect :( Try again")