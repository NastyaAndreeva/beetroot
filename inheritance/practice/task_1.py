# Exercise 1: Online Store Inventory Management
# Create a class hierarchy to represent an online store's inventory management system. 
# Start with a base class called Product and include attributes such as name, price, and quantity. 
# Create subclasses for specific types of products, such as Electronics, Clothing, and Books. 
# Each subclass should have additional attributes and methods specific to the type of product. 
# Implement methods for adding new products, updating quantities, and calculating total inventory value.

class Product:
    def __init__(self, name, price, quantity):
        self.products = []
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_product(self, **kwargs):
        self.products.append(kwargs)

    def update_quantity(self, name, new_quantity):
        for product in self.products:
            if product.get("name") == name:
                product["quantity"] = new_quantity

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product["quantity"]*product["price"]
        print(f"Total is: {total}")

class Electronics(Product):
    def __init__(self, name, price, quantity, processor):
        super().__init__(name, price, quantity)
        self.processor = processor
    
    @staticmethod
    def switch_on():
        print("You turned on your device")

class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

class Books(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

lenovo = Electronics("Lenovo", 15000, 3, "Intel I5")
dress_1 = Clothing("Red dress", 1500, 10, "S")
book_1 = Books("Python for beginners", 1000, 16, "Lutz")
print(lenovo.name)
print(lenovo.price)
print(dress_1.size)
print(book_1.author)
lenovo.switch_on()
book_1.add_product(name="Python", price=1000, quantity=3, author="Lutz")
book_1.add_product(name="JS", price=1200, quantity=5, author="Lutz")
book_1.update_quantity("JS", 20)
print(book_1.products)
book_1.calculate_total()
        