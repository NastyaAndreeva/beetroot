import random

string = input("Please, enter your string: ")
i = 1

while i <= 5:
    new_str = ""

    for n in string:
        new_str += string[random.randint(0, len(string) - 1)]

    print(new_str)
    
    i += 1