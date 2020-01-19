from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired

available_terms = [('12-month', 12), ('24-month', 24)]


class CalculatorForm(FlaskForm):

    term = SelectField('Loan Term', choices=available_terms, validators=[DataRequired()])
    loan_amount = FloatField('Loan Amount', validators=[DataRequired()],
                             render_kw={"placeholder": "Max. £20k, Min. £1k"})
    submit = SubmitField('Calculate Fee')
