def calculate(a, b):
    try:
        return int(a)**2/int(b)
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        print("You should enter numbers")

result = calculate(input("Enter first number: "), input("Enter second number: "))
print(result)