from flask import Blueprint, render_template, request, flash

from ..fee_calculator import FeeCalculator
from .forms import CalculatorForm

main = Blueprint(name='main', import_name=__name__)


@main.route('/home')
@main.route('/', methods=['GET', 'POST'])
def home():
    form = CalculatorForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            term = dict(form.term.choices).get(form.term.data)
            loan_amount = form.loan_amount.data
            fee = FeeCalculator(term, loan_amount).calculate_fee()
            loan_plus_fee = FeeCalculator(term, loan_amount).loan_plus_fee()
            if not isinstance(fee, AssertionError):
                flash(message='Your fee is £{}. It will cost you £{} at end of {} months.'
                      .format(fee, loan_plus_fee, term), category='success')
            else:
                flash(message=str(fee), category='danger')
    context = {
        'form': form
    }
    return render_template('home.html', **context)
