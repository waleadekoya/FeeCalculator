import numpy as np


class FeeCalculator:
    TERM_12M = 12
    TERM_24M = 24
    MIN_LOAN_AMT_ERROR_MSG = "The minimum loan amount is £1,000."
    MAX_LOAN_AMT_ERROR_MSG = "The maximum loan amount is £20,000."
    TERM_ERROR_MSG = "Loan term must be either 12 or 24 months."
    LOAN_AMOUNTS = [i for i in range(1000, 21000, 1000)]
    TERM_12M_FEES = [50, 90, 90, 115, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
    TERM_24M_FEES = [70, 100, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800]

    def __init__(self, term: int, loan_amount: float):
        self._term = term
        self._loan_amount = loan_amount

    @property
    def calculate_fee(self):
        try:
            self._input_validation()
            if self._loan_amount in self._fee_schedule.keys():
                fee = self._fee_schedule.get(self._loan_amount).get(self._term)
            else:
                fee = np.interp(self._loan_amount, self.LOAN_AMOUNTS, self._loan_term())
            return self._round_fee(fee)
        except AssertionError as error:
            return error

    @property
    def _fee_schedule(self):
        return {loan_amount: {self.TERM_12M: term_12_fee, self.TERM_24M: term_24_fee}
                for loan_amount, term_12_fee, term_24_fee in
                zip(self.LOAN_AMOUNTS, self.TERM_12M_FEES, self.TERM_24M_FEES)}

    def _input_validation(self):
        assert self._loan_amount >= 1000, self.MIN_LOAN_AMT_ERROR_MSG
        assert self._loan_amount <= 20000, self.MAX_LOAN_AMT_ERROR_MSG
        assert self._term == 12 or self._term == 24, self.TERM_ERROR_MSG

    def _loan_term(self):
        return self.TERM_12M_FEES if self._term == self.TERM_12M else self.TERM_24M_FEES

    def loan_plus_fee(self):
        return self._round_fee(self._loan_amount + self.calculate_fee)

    @staticmethod
    def _round_fee(num: float, base=5):
        return base * round(float(num) / base)


class LoanApplication(FeeCalculator):

    def __init__(self, term: int, loan_amount: float):
        super().__init__(term, loan_amount)


loan_fee = LoanApplication(25, 3822.22).calculate_fee
print(loan_fee)
