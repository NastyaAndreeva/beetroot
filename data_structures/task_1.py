class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def reverse_string(input_string):
    my_stack = Stack()
    for el in input_string:
        my_stack.push(el)

    reversed_string = ""
    while not my_stack.is_empty():
        reversed_string += my_stack.pop()

    return reversed_string

if __name__ == "__main__":
    input_string = input("Please, enter a sequence of characters: ")
    reversed_string = reverse_string(input_string)
    print("The reversed string:", reversed_string)