from flask import Blueprint, render_template, request, redirect

from ..fee_calculator import FeeCalculator
from .forms import CalculatorForm

main = Blueprint(name='main', import_name=__name__)


@main.route('/home')
@main.route('/', methods=['GET', 'POST'])
def home():
    fee = None
    form = CalculatorForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            term = dict(form.term.choices).get(form.term.data)
            loan_amount = form.loan_amount.data
            fee = FeeCalculator(term, loan_amount).calculate_fee()
            return 'Fee is £{}.'.format(fee) if not isinstance(fee, AssertionError) else str(fee)
    context = {
        'form': form,
        'fee': fee
    }
    return render_template('home.html', **context)
