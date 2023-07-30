class Employee:
    def __init__(self, name, department, manager, skills, english_level, salary):
        self.name = name
        self.department = department
        self.manager = manager
        self.skills = skills
        self._english_level = english_level
        self.__salary = salary

    def get_salary(self):
        return self.__salary

class Department:
    def __init__(self):
        self.__employees = []
        self.__average_salary = 0

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee):
        self.__employees.remove(employee)

    def calculate_average_salary(self):
        total = 0
        for employee in self.__employees:
            total += employee.get_salary()
        self.__average_salary = total / len(self.__employees)

    def get_average_salary(self):
        return self.__average_salary

    def get_employees(self):
        print(self.__employees)

employee_1 = Employee("Anastasiia", "IT", "Iryna", ["Python", "Django", "React"], "C1", 900000)
employee_2 = Employee("Maria", "IT", "Iryna", ["Python", "Django", "React"], "C1", 1700000)
employee_3 = Employee("Iryna", "IT", "Iryna", ["Python", "Django", "React"], "C1", 1300000)

it_department = Department()
it_department.add_employee(employee_1)
it_department.add_employee(employee_2)
it_department.add_employee(employee_3)
it_department.calculate_average_salary()
# print(it_department.get_average_salary())
# it_department.remove_employee(employee_1)
it_department.get_employees()