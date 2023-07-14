class Student:
    def __init__(self, name, age, faculty, grades):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.grades = grades
        self.average_grade = self.calculate_average_grade()

    def self_info(self):
        print(f"Student's name: {self.name}")
        print(f"Student's age: {self.age}")
        print(f"Student's faculty: {self.faculty}")
        print(f"Student's grades: {self.grades}")
        print(f"Student's average grade: {self.average_grade}")

    def calculate_average_grade(self):
        grades = list(self.grades.values())
        flat_list = [item for sublist in grades for item in sublist]
        self.average_grade = int(sum(flat_list)/len(flat_list))


student_1 = Student("John Smit", 18, "Computer science", {"math": [100,99,98], "python":[99,98,100]})
student_1.calculate_average_grade()
print(student_1.average_grade)
student_1.self_info()