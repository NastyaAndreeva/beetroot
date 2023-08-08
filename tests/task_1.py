import unittest
import employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = employee.Developer("Anastasiia", "Python Developer", 4000, ["Python", "Postgres", "React"], "Fullstack")

    def test_calculate_bonuses(self):
        self.my_employee.calculate_bonuses(25)
        self.assertEqual(self.my_employee.salary, 5000)


unittest.main()