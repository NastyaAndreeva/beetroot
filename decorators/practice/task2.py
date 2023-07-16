from functools import wraps
import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))

def add_brake_log(size=5):
    def add_brake_log_dec(func):
        counter = 0 
        # @wraps(func)
        def wrap(*args, **kwargs):
            nonlocal counter
            if counter > size:
                print("Error")
                return
            counter += 1
            return func(*args, **kwargs)
        return wrap
    return add_brake_log_dec

@add_brake_log()
def test():
    """test function docs"""
    print('inside test')
    
test()
test()
test()
test()
test()
test()
test()
print(not False)