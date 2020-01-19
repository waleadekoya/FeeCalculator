class FeeStructure:
    TERM_12M = 12
    TERM_24M = 24

    LOAN_AMOUNTS = [i for i in range(1000, 21000, 1000)]
    TERM_12M_FEES = [50, 90, 90, 115, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
    TERM_24M_FEES = [70, 100, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800]

    MIN_LOAN_AMT_ERROR_MSG = "The minimum loan amount is £1,000."
    MAX_LOAN_AMT_ERROR_MSG = "The maximum loan amount is £20,000."
    TERM_ERROR_MSG = "Loan term must be either 12 or 24 months."

    @property
    def fee_schedule(self):
        return {loan_amount: {self.TERM_12M: term_12_fee, self.TERM_24M: term_24_fee}
                for loan_amount, term_12_fee, term_24_fee in
                zip(self.LOAN_AMOUNTS, self.TERM_12M_FEES, self.TERM_24M_FEES)}
