def outer_function():
    print("This is outer function")
    def inner_function():
        print("This is inner function")
        return True
    return inner_function

print(outer_function()())