def add_order(order_list, dish_name, dish_price):
    order_list.append((dish_name, dish_price))
    return order_list

def del_order(order_list, dish_name):
    idx = 0
    for order in order_list:
        if (order[0] == dish_name):
            order_list.pop(idx)
            return order_list
        idx +=1

def calculate_total(order_list):
    total = 0
    for order in order_list:
        total += order[1]

    return total