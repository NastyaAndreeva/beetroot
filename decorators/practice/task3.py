from functools import wraps

def reverse_boolean_value(func):
    @wraps(func)
    def reverse_wrapper(a):
        if type(a)==int or type(a)==float:
            return False
        else:
            return True
    return reverse_wrapper
    
@reverse_boolean_value
def is_number(a):
    return type(a)
print(is_number(6))