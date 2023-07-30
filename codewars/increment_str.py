def increment_string(string):
    num = ""
    if string[-1].isdigit() and string[-1] != "9":
            return string[0:-1] + str(int(string[-1]) + 1)
    for n in range(-1, -(len(string) + 1),-1):
        if string[n].isdigit():
            num += string[n]
        else:
            break
    print(num[::-1])
    # return string[0:-len(num)] + str(int(num[::-1]) + 1)

print(increment_string("foo"))
print(increment_string("foo23"))
print(increment_string("foobar00999"))
