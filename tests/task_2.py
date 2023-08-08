# Write tests for the Phonebook application, which you have implemented in module 1. 
# Design tests for this solution and write tests using unittest library
import unittest
import dictionary

class TestDictionary(unittest.TestCase):
    # def setUp(self):
    #     self.my_employee = employee.Developer("Anastasiia", "Python Developer", 4000, ["Python", "Postgres", "React"], "Fullstack")

    def test_calculate_bonuses(self):
        result = dictionary.search_by_field()
        print(result)


unittest.main()