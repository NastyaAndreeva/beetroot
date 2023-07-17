class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        try:
            self.products[product.name] = {
                "type": product.type,
                "price": round(product.price * 1.3,2),
                "amount": amount
            }
        except ValueError:
            print("The info about product is invalid")

    def set_discount(self, identifier, percent, identifier_type='name'):
        for key, value in self.products.items():
            if identifier_type == "name":
                self.products[identifier]["price"] = round(self.products[identifier]["price"] * (1 - percent/100), 2)
            else:
                if value["type"] == identifier:
                    value["price"] = round(value["price"]*(1 - percent/100), 2)

    def sell_product(self, product_name, amount):
        try:
            for product in self.products:
                if product == product_name:
                    self.products[product_name]["amount"] -= amount
                    self.income += self.products[product_name]["amount"] * self.products[product_name]["price"]
        except ValueError:
            print("The info about order is incorrect")
 
    def get_income(self):
        return self.income
    
    def get_all_products(self):
        return self.products
    
    def get_product_info(self, product_name):
        try:
            for product in self.products:
                if product == product_name:
                    return (product_name, self.products[product_name]["amount"])
        except ValueError:
            print("The value is invalid")

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
s.set_discount("Ramen", 10)
print(s.get_product_info('Ramen'))
print(s.get_all_products())