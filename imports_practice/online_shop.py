def statistics(my_list):
    new_dict = {}
    for item in my_list:
        if not new_dict.get(item[0]):
            new_dict[item[0]] = 1
        else:
            new_dict[item[0]] += 1
    
    sorted_dict = sorted(new_dict.items(), key=lambda x:x[1])
    
    return sorted_dict