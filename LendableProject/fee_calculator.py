import numpy as np

from .fee_structure import FeeStructure, ErrorMessages

__author__ = "Wale Adekoya"
__revision__ = "Version 1.0.0"


class FeeCalculator(FeeStructure, ErrorMessages):

    """
    This class implements a Fee Calculator that calculates a fee according
    the fee structure defined in class 'FeeStructure'.

    This class is then wrapped in a simple flask micro-web framework
    to expose an API to this calculator
    """

    def __init__(self, term: int, loan_amount: float):
        self._term = term
        self._loan_amount = loan_amount

    def calculate_fee(self):
        """
        :param: None
        :return: calculated fee based on loan_term and loan_amount or
        Assertion error message if any of the requirements for loan amount and/or
        loan term has not been met.

        Values in between the breakpoints is linearly interpolated
        using numpy between the lower bound and upper bound that they
        between.
        """
        try:
            self._input_validation()
            if self._loan_amount in self.fee_schedule.keys():
                fee = self.fee_schedule.get(self._loan_amount).get(self._term)
            else:
                fee = np.interp(self._loan_amount, self.LOAN_AMOUNTS, self._loan_term())
            return self._round_fee(fee)
        except AssertionError as error:
            return error

    def _input_validation(self):
        """
        Implements the requirements that:
        a) the minimum loan amount shall be £1,000;
        b) the maximum loan amount shall not exceed £20,000
        c) The term can either be 12 or 24 months.
        :return: assertion error if any of the requirements is not met.
        """
        assert self._loan_amount >= 1000, self.MIN_LOAN_AMT_ERROR_MSG
        assert self._loan_amount <= 20000, self.MAX_LOAN_AMT_ERROR_MSG
        assert self._term == 12 or self._term == 24, self.TERM_ERROR_MSG

    def _loan_term(self):
        return self.TERM_12M_FEES if self._term == self.TERM_12M else self.TERM_24M_FEES

    def loan_plus_fee(self):
        """
        fulfil the requirements that the fee shall be rounded such that
        (fee + loan amount) is an exact multiple of 5.
        :return: (fee + loan amount) rounded to multiple of 5.
        """
        if isinstance(self.calculate_fee(), AssertionError):
            return str(self.calculate_fee())
        else:
            return self._round_fee(self._loan_amount + self.calculate_fee())

    @staticmethod
    def _round_fee(num: float, base=5):
        """
        :param num: accepts any float number
        :param base: the base to round to
        :return: rounded amount that is an exact multiple of the given base
        """
        return base * round(float(num) / base)


class LoanApplication(FeeCalculator):
    """
    :param: term - loan duration
    :param: loan_amount - total loan amount
    """

    def __init__(self, term: int, loan_amount: float):
        super().__init__(term, loan_amount)


"loan_fee = LoanApplication(24, 382285).loan_plus_fee(); print(loan_fee)"
