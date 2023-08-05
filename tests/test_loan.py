import loan
import unittest
from unittest.mock import Mock

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.my_loan = loan.PersonalLoan(13, 38000, 7, 18, "Mel", "Robbins", "+48888888888", 100000)

    def test_total_repayment(self):
        mock_total_repayment = Mock()
        mock_total_repayment.return_value = 40660
        result = self.my_loan.calculate_total_repayment()
        self.assertEqual(mock_total_repayment(), result)

    def test_calculate_interest_amount(self):
        mock_interest_amount = Mock()
        mock_interest_amount.return_value = 2660
        interest_amount = self.my_loan.calculate_interest_amount()
        self.assertEqual(mock_interest_amount(), interest_amount)

unittest.main()