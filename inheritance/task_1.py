class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_info(self):
        print(f"Your name is {self.last_name} {self.first_name}")
        print(f"Your email is {self.email}")


class Student(Person):
    def __init__(self, first_name, last_name, email, scores):
        super().__init__(first_name, last_name, email)
        self.scores = scores

    def calculate_average_grade(self):
        grades = list(self.grades.values())
        flat_list = [item for sublist in grades for item in sublist]
        self.average_grade = int(sum(flat_list)/len(flat_list))

class Teacher(Person):
    def __init__(self, first_name, last_name, email, salary, classes):
        super().__init__(first_name, last_name, email)
        self.salary = salary
        self.classes = classes

    def get_promotion(self, idx_increase):
        self.salary *= 1 + idx_increase/100

student_1 = Student("Alex", "Smith", "smith@gmail.com", {"math": [99, 100, 99]})
print(student_1.scores)
teacher_1 = Teacher("David", "Malan", "malan@hvd.com", 120000, ["Computer Science", "Python", "Math"])
teacher_1.print_info()
teacher_1.get_promotion(10)
print(teacher_1.salary)