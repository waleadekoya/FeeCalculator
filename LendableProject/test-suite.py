import unittest

from fee_calculator import LoanApplication


class FeeCalculatorTest(unittest.TestCase):

    """
    A test suite to validate the implemented solution for the Fee Calculator.
    """

    def test_loan_fee(self):
        self.assertEqual(LoanApplication(24, 2750).calculate_fee(),
                         115)

    def test_min_loan_amt(self):
        application = LoanApplication(24, 850)
        self.assertEqual(str(application.calculate_fee()), str(AssertionError(LoanApplication.MIN_LOAN_AMT_ERROR_MSG)))

    def test_max_loan_amt(self):
        application = LoanApplication(24, 112750)
        self.assertEqual(str(application.calculate_fee()), str(AssertionError(LoanApplication.MAX_LOAN_AMT_ERROR_MSG)))

    def test_loan_term(self):
        application = LoanApplication(55, 20000)
        self.assertEqual(str(application.calculate_fee()), str(AssertionError(LoanApplication.TERM_ERROR_MSG)))

    def test_loan_plus_fee(self):
        application = LoanApplication(24, 2750)
        self.assertEqual(application.loan_plus_fee(), (115 + 2750))

    def test_loan_plus_fee_is_multiple_of_5(self):
        application = LoanApplication(24, 2750)
        self.assertEqual(application.loan_plus_fee() % 5 == 0, (115 + 2750) % 5 == 0)


if __name__ == "__main__":
    unittest.main()
