my_string = input("Please, enter your string: ")
my_list = my_string.lower().split(" ")
my_set = set(my_list)
my_dict = {}

for item in my_set:
    my_dict[item] = my_list.count(item)

print(my_dict)
