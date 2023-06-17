init_list = list(range(1, 101))
new_list = []
i = 0

while i < 100:
    if (init_list[i] % 7 == 0 and init_list[i] % 5 != 0):
        new_list.append(init_list[i])
    i += 1

print(new_list)