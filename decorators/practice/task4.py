from functools import wraps

def check_type_of_arguments(func):
    @wraps(func)
    def check_wrapper(*args):
        for el in args:
            if not type(el)==str:
                print("Error")
                return
        print("All elements passed the checker")
    return check_wrapper

@check_type_of_arguments
def print_strings(*args):
    for el in args:
        print(el)

print_strings("Sunshine","cloudy","icloud", 5)