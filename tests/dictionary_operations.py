def add_entry(phonebook_list, first_name, last_name, city, phone):
    name = first_name + " " + last_name
    phonebook_list.append({name: {"city": city, "phone": phone}}) 
    return phonebook_list

def update_entry(phonebook_list, phone, field, new_value):
    for item in phonebook_list:
        for value in item.values():
            if value["phone"] == phone:
                value[field] = new_value
                return phonebook_list

def search_by_name(phonebook_list, name):
    sorted_list = []
    for item in phonebook_list:
        if item.get(name) != None:
            sorted_list.append(item)
    return sorted_list

def search_by_field(phonebook_list, field, value):
    for item in phonebook_list:
        for el in item.values():
            if el.get(field) == value:
                return item

def delete_entry(phonebook_list, phone):
    for item in phonebook_list:
        for value in item.values():
            if value["phone"] == phone:
                phonebook_list.remove(item)
                return phonebook_list