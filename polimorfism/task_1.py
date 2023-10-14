class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def talk():
        print("I am talking")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def talk():
        print("meow meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def talk():
        print("woof woof")

def gen_func(animal):
    animal.talk()

cat_1 = Cat("Tomas")
dog_1 = Dog("Max")
gen_func(cat_1)
gen_func(dog_1)