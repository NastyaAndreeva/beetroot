def calculate(number_1, number_2, operation):
    if (not number_1.isdigit() or not number_2.isdigit()):
        return "Only numbers are allowed"
    number_1 = int(number_1)
    number_2 = int(number_2)
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        return "Incorrect operation"