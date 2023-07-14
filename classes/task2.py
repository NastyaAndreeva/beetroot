class Dog:
    age_factor = 7
    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor

dog_1 = Dog(3)
print(dog_1.human_age())