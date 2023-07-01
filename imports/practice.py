import product_operations
import student_marks
import orders
from task_operations import add_task, update_status
from create_multiple_emails import create_multiple_emails
from calculator import calculate
# Task 1
my_dict={}

# product_operations.add_product(my_dict,"Milk",10,5)
# product_operations.add_product(my_dict,"Bread",20,4)
# product_operations.add_product(my_dict,"Sushi",200,3)
# product_operations.update_product(my_dict,"Milk","cost",14)
# product_operations.print_product_cost(my_dict)

# Task 2
tasks_list = {}

# add_task(tasks_list, "Learn functions", "args and kwargs", 8, "in progress")
# add_task(tasks_list, "Github", "Manage settings", 5, "Completed")
# update_status(tasks_list, "learn functions", "Completed")

# Task3

# result = calculate(input("Enter first number: "), input("Enter second number: "), input("Enter your operation: +, -, *, /: "))
# print(result)
# Task 4


# print(create_multiple_emails([["andriy", "zavora", "@gmail.com"], ["sergii", "troichuk", "@gmail.com"], ["anastasiia", "andrieieva", "@gmail.com"], ["maxim", "kostenko", "@gmail.com"]]))

# Task 6
new_dict = {}
# student_marks.add_mark(new_dict, "Maria", 100)
# student_marks.add_mark(new_dict, "Maria", 98)
# student_marks.add_mark(new_dict, "Maria", 99)
# student_marks.add_mark(new_dict, "Anastasiia", 100)
# student_marks.delete_mark(new_dict, "Maria", 98)
# print(student_marks.calculate_average(new_dict, "Maria"))
# student_marks.print_marks(new_dict)

# Task 7
order_list = []
orders.add_order(order_list, "Sushi", 250)
orders.add_order(order_list, "Ramen", 180)
orders.add_order(order_list, "Pizza", 230)
orders.add_order(order_list, "Cake", 130)
print(order_list)
orders.del_order(order_list, "Pizza")
print(order_list)
print(orders.calculate_total(order_list))
