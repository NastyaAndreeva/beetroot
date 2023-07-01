from statistics import mean

# task1

# my_dict = {"pr_1": {"price": 10}, "pr_2": {"price": 20}}

# pr_name = input("Enter product name: ")
# pr_property = input("Enter product property: ")
# pr_value = input("Enter property value: ")

# my_dict[pr_name] = {pr_property: pr_value}

# print(my_dict)

# task6

# scores = {"student_1": [100, 98, 99], "student_2": [85, 89, 84]}
# for key, value in scores.items():
#     print(key, ": ", value)
#     print(key, ": ", mean(value))

# operation = input("Please, choose update (u) or delete (d): ")
# if operation.lower() == "u":
#     student_name = input("Please, enter student name: ")
#     student_mark = input("Please, enter new mark: ")
#     if not student_mark.isnumeric:
#         print("The mark must be a number")
#     else:
#         scores[student_name].append(int(student_mark))
#         print(scores)
# elif operation.lower() == "d":
#     student_name = input("Please, enter student name: ")
#     student_mark = input("Please, enter the mark you want to delete: ")
#     if not student_mark.isnumeric:
#         print("The mark must be a number")
#     else:
#         scores[student_name].remove(int(student_mark))
#         print(scores)
# else:
#     print("The operation is not correct")

# task7
# Створіть програму для управління замовленнями в ресторані. 
# Використовуйте list для зберігання замовлень, де кожне замовлення представлене як tuple з назвою страви і ціною. 
# Реалізуйте можливість додавання нових замовлень, видалення замовлень і розрахунку загальної суми замовлення.

# orders = [("sushi", 250), ("ramen", 180)]
# dish_name = input("Please, enter the dish name: ")
# dish_price = input("Please, enter the dish price: ")
# orders.append((dish_name, int(dish_price)))
# print(orders)
# total = 0
# for order in orders:
#     total += order[1]
# print(total)

# Task 8
# У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. 
# Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. Надайте дані по наступним моментах:
# - Які 3 продукти ваші клієнти купують найчастіше
# - Які 3 продукти ваші клієнти купують найрідше?
# - Скільки разів клієнти купували кожен з ваших продуктів?
# orders = [{ "milk": 2, "bread": 5}, {"butter": 3, "milk": 1}]
# products = set()
# for item in orders:
#     products.update(set(item.keys()))

# print(products)
# products_dict = {item: 0 for item in products}

# for product in products_dict:
#     for order in orders:
#         if order.get(product) != None:
#             products_dict[product] += order.get(product)
        

# print(products_dict)

# task9

# schedule = [("Computer science", "Monday"), ("Math", "Tuesday"), ("English", "Wednesday")]
# for item in schedule:
#     print(item[0], ": ", item[1])

# operation = input("Please, choose your operation: add (a) or delete (d)")

# if operation.lower() == "a" or operation.lower() == "add":
#     new_subject = input("Please, enter the subject and day: ").split(" ")
#     schedule.append((new_subject[0], new_subject[1]))
# elif operation.lower() == "d" or operation.lower() == "delete":
#     remove_subject = input("Please, enter the subject and day for deleting: ").split(" ")
#     schedule.remove((remove_subject[0], remove_subject[1]))
# else:
#     print("The operation is not correct")

# print(schedule)

# Task10
# Створіть програму для керування списком завдань. Використовуйте множину (set) для зберігання завдань, 
# які потрібно виконати. Реалізуйте для користувача можливість додавання нових завдань, видалення завдань і перевірку, 
# чи всі завдання виконані. 
# (тобто користувач повинен мати змогу виконувати ці всі завдання через інпут з терміналу)

tasks = {("task1", False), ("task2", False), ("task3", True)}

for task in tasks:
    if not task[1]:
        print("Not all assignments are completed")
        break

operation = input("Please, choose your operation: add (a) or delete (d): ")
if operation.lower() == "a" or operation.lower() == "add":
    new_task = input("Please, enter the task and status: ").split(" ")
    tasks.add((new_task[0], bool(new_task[1])))
elif operation.lower() == "d" or operation.lower() == "delete":
    remove_task = input("Please, enter the task and status for deleting: ").split(" ")
    schedule.remove((remove_task[0], bool(remove_task[1])))
else:
    print("The operation is not correct")

print(tasks)





