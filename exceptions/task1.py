def oops():
    raise IndexError
    # raise KeyError #2 exceptions will occur

def print_elem(my_list):
    try:
        print(my_list[10])
    except IndexError:
        oops()

print(print_elem([1,2,3]))