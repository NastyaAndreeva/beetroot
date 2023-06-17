import random

first_list = []
second_list = []

while len(first_list) != 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))

new_list = list(set(first_list).union(set(second_list)))

print(first_list)
print(second_list)
print(new_list)