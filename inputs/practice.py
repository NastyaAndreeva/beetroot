# # Task1
# name = input("Please, enter your name: ")
# surname = input("Please, enter your surname: ")

# print(f"{name.lower()}.{surname.lower()}@kobzar.com")

#Task2

# counter = 0

# while counter < 5:
#     input("Should I call you?: ")
#     counter += 1
# else:
#     print("Have a nice day")

# Task3

# while True:
#     reply = input("Should I call you? Please, enter 'y' or 'n' ")
#     if reply.lower() == "n":
#         print("Have a nice day")
#         break

# Task4

# while True:
#     customers_number = input("Please, enter the number of customers, it must be a digit: ")
#     if not customers_number.isnumeric():
#         customers_number = input("Please, enter the number of customers, it must be a digit (inside if): ")
#     else:
#         for i in range(1, int(customers_number)):
#             if (i % 15 == 0):
#                 print("You've got a pen")
#                 print("You've got a ruler")
#             elif (i % 3 == 0):
#                 print("You've got a pen")
#             elif (i % 5 == 0):
#                 print("You've got a ruler")
#             else:
#                 print("Try again... Not your day :(")
#         break

# Task5

# income = int(input("Please, enter your income: "))
# age = int(input("Please, enter your age: "))
# is_employed = input("Please, enter your employment status 'y' or 'n': ") 

# if income >= 10000 and is_employed.lower() == "y":
#     if age >= 18 and age <= 60:
#         print("You can get a loan")
#     else:
#         print("Sorry, you can't get a loan")
# else:
#     print("Sorry, you can't get a loan. Come again when you get a work or promotion")

# Task6

# 1) length >= 8
# 2) for i in string, i.isnumeric() - чи число
# 3) for i in string, i.upper() == i - capital letter
# 4) special symbol not c.isalnum()

user_password = input("Please, enter your password. The password must include at least 1 capital letter, special symbol, and 1 number. The min length is 8: ")
has_number = False
has_capital = False
has_special = False

if len(user_password) < 8:
    print("The password is too short")
else:
    for i in user_password:
        if i.isnumeric():
            has_number = True
        elif i.upper() == i:
            has_capital = True
        elif not i.isalnum():
            has_special = True

    if has_capital and has_number and has_special:
        print("Your password is super")


