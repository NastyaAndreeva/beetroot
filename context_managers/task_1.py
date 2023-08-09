class FileManager:
    counter = 0

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, file_path, mode="r"):
        self.file = None
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        self.counter += 1

        print("-------Enter file-----")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_cb):
        print(f"Current counter is {self.counter}")
        print("-------Exit file------")
        if self.file != None:
            self.file.close()
        return None

if __name__ == "__main__":
    with FileManager("task_1.txt") as file:
        print(file.read())