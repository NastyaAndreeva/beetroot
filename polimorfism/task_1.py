class Animal:
    @staticmethod
    def talk():
        print("Basic talk")

class Dog(Animal):
    @staticmethod
    def talk():
        print("woof woof")

class Cat(Animal):
    @staticmethod
    def talk():
        print("meow")

def talk(animal):
    animal.talk()

dog_1 = Dog()
cat_1 = Cat()

talk(dog_1)
talk(cat_1)
