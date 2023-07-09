def define_number_of_local_vars(a, b):
    count = 0
    for _ in locals():
        count += 1
    return count

print(define_number_of_local_vars(3, 4))