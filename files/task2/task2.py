import json
from dictionary_operations import add_entry, update_entry, search_by_field, search_by_name, delete_entry

try:
    with open("phonebook.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    raise FileNotFoundError

def writer_wrapper():
    try:
        with open("phonebook.json", "w+") as file:
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError

operation = input("Please, type the operation that you want to implement: add (a), update (u), search (s), delete (d), or exit (e): ")

if (operation.lower() == "a" or operation.lower() == "add"):
    add_entry(data, input("Please, enter first name: "), input("Please, enter last name: "), input("Please, enter your city: "), input("Please, enter your phone: "))
    writer_wrapper()
elif (operation.lower() == "u" or operation.lower() == "update"):
    update_entry(data,"+6666666668", "city", "Munchen")
    writer_wrapper()
elif (operation.lower() == "s" or operation.lower() == "search"):
    print(search_by_field(data, "city", "Tokyo"))
    print(search_by_field(data, "phone", "+6666666668"))
    print(search_by_name(data, "Kaiser Michael"))
elif (operation.lower() == "d" or operation.lower() == "delete"):
    delete_entry(data, "+6666666666")
    writer_wrapper()
elif (operation.lower() == "e" or operation.lower() == "exit"):
    pass
else:
    print("The operation is invalid")