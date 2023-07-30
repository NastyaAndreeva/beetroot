import sys
sys.set_int_max_str_digits(640)

def sum_strings(x, y):
    if x == "" and y == "":
        return "0"
    elif x == "":
        return str(0 + int(y))
    elif y == "":
        return str(0 + int(x))
    else:
        return str(float(x) + float(y))

print(sum_strings("123", "456"))
print(sys.get_int_max_str_digits())