class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def get_from_stack(self, element):
        if element in self.items:
            return element
        else:
            raise ValueError(f"Element {element} not found in the stack")

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise ValueError("Queue is empty")

    def get_from_queue(self, element):
        if element in self.items:
            return element
        else:
            raise ValueError(f"Element {element} not found in the queue")

    def is_empty(self):
        return len(self.items) == 0

# Using the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

try:
    result = stack.get_from_stack(2)
    print(f"Element found: {result}")
except ValueError as e:
    print(e)

try:
    result = stack.get_from_stack(4)
    print(f"Element found: {result}")
except ValueError as e:
    print(e)