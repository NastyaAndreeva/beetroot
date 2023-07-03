def add_product(my_dict, name,cost,quantity):
    my_dict[name]={"cost":cost,"quantity":quantity}

def update_product(my_dict,name,my_property,property_value):
    my_dict[name][my_property]=property_value

def print_product_cost(dict):
    for key,value in dict.items():
        print(f"{key}: {value['cost']}")