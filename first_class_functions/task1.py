def define_number_of_local_vars(a, b):
    count = 0
    return len(locals())

print(define_number_of_local_vars(3, 4))