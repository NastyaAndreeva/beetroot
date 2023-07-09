def is_number_digit(func):
    def number_wrapper(number):
        if number.isdigit():
            return func(number)
        else:
            print(False)
            return
    return number_wrapper

@is_number_digit
def print_elements(a):
    print(a)

print_elements("a")