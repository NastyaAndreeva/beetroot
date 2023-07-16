class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.attendance = 1

    def calculate_bonuses(self, bonus):
        self.salary *= 1 + bonus/100
        print(self.salary)

    def get_report(self):
        print("Your name is: " + self.name)
        print("Your position is: " + self.position)
        print("Your salary is: " + str(self.salary))

    def increase_attendance(self):
        self.attendance += 1
        

class Manager(Employee):
    def __init__(self, name, position, salary, project):
        super().__init__(name, position, salary)
        self.project = project

class Developer(Employee):
    def __init__(self, name, position, salary, skills, direction):
        super().__init__(name, position, salary)
        self.skills = skills
        self.direction = direction

class Salesperson(Employee):
    def __init__(self, name, position, salary, sales_quantity):
        super().__init__(name, position, salary)
        self.sales_quantity = sales_quantity

developer_1 = Developer("Iryna Hunko", "Developer", 1000000, ["Python", "Github"], "Backend")
# print(developer_1.direction)
developer_1.calculate_bonuses(50)
developer_1.get_report()
developer_1.increase_attendance()
developer_1.increase_attendance()
developer_1.increase_attendance()
developer_1.increase_attendance()
print(developer_1.attendance)