# def add(a):
#     def inner(b):
#         return a + b
#     return inner

class add(int):
    def __call__(self, value):
        return add(self + value)

print(add(2)(1)(10))