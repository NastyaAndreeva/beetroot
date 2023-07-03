import json

file = open("processors.json", "r")
init_data = json.load(file)
file.close()

def print_data(data):
    for el in data:
        print(el)

def get_unique_locations(data):
    locations = []
    for el in data:
        if el["location"] not in locations:
            locations.append(el["location"])

    return sorted(locations)

def modify_processor_name(new_name, data):
    for el in data:
        if el["processor"] == "AMD Ryzen":
            el["processor"] = new_name
    return json.dumps(data, indent=4)

def delete_name(deleted_name, data):
    for el in data:
        if deleted_name.lower() in el["location"].lower():
            data.remove(el)
    return json.dumps(data, indent=4)
    
# print_data(data)
# print(get_unique_locations(data))
# print_data(get_unique_locations(data))


with open("processors.json", "w+") as outfile:
        outfile.write(modify_processor_name("AMD Ryzen 2", init_data))

with open("processors.json", "w+") as outfile:
        outfile.write(delete_name("Moscow", init_data))

