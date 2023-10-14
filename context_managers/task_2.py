import unittest
import task_1

class TestContextManager(unittest.TestCase):
    def setUp(self):
        self.context_manager = task_1.FileManager("task_2.txt")

    def test_reading(self):
        result = None
        try:
            with self.context_manager as file:
                result = file.read()
        except FileNotFoundError:
            print("The file is not found")
        self.assertEqual(result, "Context managers")
            

unittest.main()