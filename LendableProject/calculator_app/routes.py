from flask import Blueprint, render_template, request, flash, jsonify

from ..fee_calculator import FeeCalculator
from .forms import CalculatorForm
from ..fee_structure import FeeStructure

main = Blueprint(name='main', import_name=__name__)


@main.route('/home')
@main.route('/', methods=['GET', 'POST'])
def home():
    form = CalculatorForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            term = dict(form.term.choices).get(form.term.data)
            print(form.term.choices, ": ", form.term.data)
            loan_amount = form.loan_amount.data
            calculator = FeeCalculator(term, loan_amount)
            fee = calculator.calculate_fee()
            loan_plus_fee = calculator.loan_plus_fee()
            if not isinstance(fee, AssertionError):
                flash(message=f'Your fee is £{fee}. It will cost you £{loan_plus_fee} at end of {term} months.',
                      category='success')
            else:
                flash(message=str(fee), category='danger')
    context = {
        'form': form
    }
    return render_template('home.html', **context)


@main.route("/fees/<term>")
def fees(term):
    _fees: list = FeeStructure.TERM_12M_FEES if term == '12-month' else FeeStructure.TERM_24M_FEES
    return jsonify(dict(fees=_fees))
