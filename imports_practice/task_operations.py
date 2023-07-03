def add_task(tasks_list, name, description, priority, status):
    tasks_list[name] = {
        "description": description,
        "priority": priority,
        "status": status
    }

def update_status(tasks_list, name, new_status):
    for key, value in tasks_list.items():
        if key.lower() == name.lower():
            value["status"] = new_status