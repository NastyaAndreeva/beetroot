def add_mark(my_dict, student_name, mark):
    if my_dict.get(student_name) == None:
        my_dict[student_name] = [mark]
    else:
        my_dict[student_name].append(mark)
    return my_dict

def delete_mark(my_dict, student_name, mark):
    if my_dict.get(student_name) == None:
        return f"The student with name {student_name} does not exist"
    else:
        my_dict[student_name].remove(mark)

    return my_dict

def calculate_average(my_dict, student_name):
    if my_dict.get(student_name) == None:
        return f"The student with name {student_name} does not exist"
    else:
        total = 0
        # sum(my_dict[student_name])
        for mark in my_dict[student_name]:
            total += mark
        return total/len(my_dict[student_name])

def print_marks(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")