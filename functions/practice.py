# Task 1
my_dict={}
def add_product(name,cost,quantity):
    my_dict[name]={"cost":cost,"quantity":quantity}

def update_product(name,my_property,property_value):
    my_dict[name][my_property]=property_value

def print_product_cost(dict):
    for key,value in dict.items():
        print(f"{key}: {value['cost']}")

# add_product("Milk",10,5)
# add_product("Bread",20,4)
# add_product("Sushi",200,3)
# update_product("Milk","cost",14)
# print(my_dict)
# print_product_cost(my_dict)

# Task 2
tasks_list = {}

def add_task(name, description, priority, status):
    # tasks_list.append([name, description, priority, status])
    tasks_list[name] = {
        "description": description,
        "priority": priority,
        "status": status
    }

def update_status(name, new_status):
    for key, value in tasks_list.items():
        # if task[0].lower() == name.lower():
        #     task[3] = new_status
        if key.lower() == name.lower():
            value["status"] = new_status

# add_task("Learn functions", "args and kwargs", 8, "in progress")
# add_task("Github", "Manage settings", 5, "Completed")
# update_status("learn functions", "Completed")
# print(tasks_list)

# Task 4

def create_email(list):
    return f"{list[0].lower()}{list[1].lower()}{list[2].lower()}"


# print(create_email(["andriy", "zavora", "@gmail.com"]))
# Task 5
def create_multiple_emails(lists):
    new_list = []
    for my_list in lists:
        new_list.append(create_email(my_list))
    
    return new_list


# print(create_multiple_emails([["andriy", "zavora", "@gmail.com"], ["sergii", "troichuk", "@gmail.com"], ["anastasiia", "andrieieva", "@gmail.com"], ["maxim", "kostenko", "@gmail.com"]]))

# Task6