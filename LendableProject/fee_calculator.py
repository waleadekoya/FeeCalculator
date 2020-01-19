import numpy as np

from .fee_structure import FeeStructure


class FeeCalculator(FeeStructure):

    def __init__(self, term: int, loan_amount: float):
        self._term = term
        self._loan_amount = loan_amount

    def calculate_fee(self):
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
        assert self._loan_amount >= 1000, self.MIN_LOAN_AMT_ERROR_MSG
        assert self._loan_amount <= 20000, self.MAX_LOAN_AMT_ERROR_MSG
        assert self._term == 12 or self._term == 24, self.TERM_ERROR_MSG

    def _loan_term(self):
        return self.TERM_12M_FEES if self._term == self.TERM_12M else self.TERM_24M_FEES

    def loan_plus_fee(self):
        return self._round_fee(self._loan_amount + self.calculate_fee())

    @staticmethod
    def _round_fee(num: float, base=5):
        return base * round(float(num) / base)


class LoanApplication(FeeCalculator):

    def __init__(self, term: int, loan_amount: float):
        super().__init__(term, loan_amount)


loan_fee = LoanApplication(24, 3822.22).calculate_fee()
print(loan_fee)
