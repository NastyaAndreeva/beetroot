class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def get_promotion(self, new_position):
        self.position = new_position

    def salary_increase(self, idx_increase):
        self.salary *= idx_increase
        print(f"Congrats, your salary was increased in {idx_increase} times")

employee_1 = Employee("Maria", 1000000, "engineer")
# print(employee_1.position)
employee_1.get_promotion("software engineer")
# print(employee_1.position)
# employee_1.salary_increase(3)
# print(employee_1.salary)
employee_2 = Employee("Anastasiia", 1000000, "React engineer")
print(employee_2.position)
employee_2.get_promotion("Senior engineer")
print(employee_2.position)