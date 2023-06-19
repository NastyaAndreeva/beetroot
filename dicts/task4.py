my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
first_dict = {day: idx + 1 for idx, day in enumerate(my_list)}
second_dict = {idx + 1: day  for idx, day in enumerate(my_list)}

print(first_dict)
print(second_dict)