phone_number = "1112223434"
is_valid = True

if len(phone_number) != 10:
    print("Please, check the phone number. The length must contain 10 numbers")
else:
    for number in phone_number:
        if not number.isnumeric():
            is_valid = False
    
    if is_valid:
        print(f"{phone_number} is valid :)")
    else:
        print("Please, check the phone number. It must contain only numbers")
