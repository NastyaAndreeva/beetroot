import csv

def update_phone(last_name, phone, data_reader):
    data = list(data_reader)
    new_data = []
    for el in data:
        if el != []:
            new_data.append(el)
    for el in new_data:
        if len(el) != 1 and el[1] == last_name:
            el[3]=phone
    return new_data

def delete_el(last_name, data_reader):
    data = list(data_reader)
    print(data)
    new_data = []
    for el in data:
        if el != []:
            new_data.append(el)
    for el in new_data:
        if el[1] == last_name:
            print("inside if")
            new_data.remove(el)
    return new_data

def update_phone_dict(my_dict, last_name, phone):        
    for item in my_dict:
        if item["Surname"] == last_name:
            print("inside")
            item["Phone"] = phone
    return my_dict

fields = ["Name","Surname","Age","Phone","City","Country","Department","Position"]
with open("nestle_employee.csv", newline='') as outfile:
    reader = csv.DictReader(outfile, fieldnames=fields)
    writer = csv.DictWriter(outfile, fieldnames=fields)
    data = update_phone_dict(reader, "Smith", "+8 1234567890")
    print(type(data))
    for el in data:
        print("1")
        # print(el)
        # writer.writerow(el)
    
    # outfile.write(data)
    
    # writer = csv.writer(outfile, "w")
    # writer.writerows(data)

# data_reader = csv.reader(open("nestle_employee.csv"))
# data = update_phone("Smith", "+8 1234567890", data_reader)
# writer = csv.writer(open("nestle_employee.csv", "w"))
# writer.writerows(data)

# data_reader = csv.reader(open("nestle_employee.csv"))
# data_del = delete_el("Johnson", data_reader)
# writer = csv.writer(open("nestle_employee.csv", "w"))
# writer.writerows(data_del)