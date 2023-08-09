import unittest
import dictionary

class TestDictionary(unittest.TestCase):
    def test_operation(self):
        result = dictionary.run_dictionary()
        self.assertAlmostEqual(result, "Success")


unittest.main()