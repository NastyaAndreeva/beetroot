def logger(func):
    def wrapper_func(*args):
        list_strs = [str(arg) for arg in args]
        print(func.__name__ + " called with", ", ".join(list_strs))
    return wrapper_func

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(10, 23)
square_all(1, 2, 3, 4)
