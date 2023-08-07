class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Fraction(self.value + other.value)

    def __sub__(self, other): 
        return Fraction(self.value - other.value)

    def __mul__(self, other): 
        return Fraction(self.value * other.value)

    def __div__(self, other): 
        return Fraction(self.value / other.value)

    def __str__(self): 
        return str(self.value)

if __name__ == "__main__":
    x = Fraction(1)
    y = Fraction(4)
    print(x)
    print(y)
    print(x + y)