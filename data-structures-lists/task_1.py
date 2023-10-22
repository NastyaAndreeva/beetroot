from node import Node

class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        self.add(item)

    def index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError(f"{item} is not in the list")

    def pop(self, index=None):
        if index is None:
            if self.is_empty():
                raise IndexError("You are trying to pop from empty list")
            current = self._head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            if previous is None:
                self._head = None
            else:
                previous.set_next(None)
            return current.get_data()
        else:
            if index < 0:
                index += self.size()
            if index < 0 or index >= self.size():
                raise IndexError("Pop index is out of range")
            current = self._head
            previous = None
            i = 0
            while i < index:
                previous = current
                current = current.get_next()
                i += 1
            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())
            return current.get_data()

    def insert(self, index, item):
        if index < 0:
            index += self.size()
        if index < 0 or index > self.size():
            raise IndexError("Insert index is out of range")

        if index == 0:
            self.add(item)
        else:
            current = self._head
            previous = None
            i = 0
            while i < index:
                previous = current
                current = current.get_next()
                i += 1
            temp = Node(item)
            if previous is None:
                self._head = temp
            else:
                previous.set_next(temp)
            temp.set_next(current)

    def slice(self, start, stop):
        if start < 0:
            start += self.size()
        if stop < 0:
            stop += self.size()

        if start < 0 or start >= self.size():
            raise IndexError("Slice start index is out of range")
        if stop < 0 or stop > self.size():
            raise IndexError("Slice stop index is out of range")
        if start >= stop:
            raise ValueError("Slice start index must be less than slice stop index")

        current = self._head
        result = UnsortedList()
        i = 0
        while i < stop:
            if i >= start:
                result.add(current.get_data())
            current = current.get_next()
            i += 1

        return result

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"
