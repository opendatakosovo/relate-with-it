from wtforms import Form, StringField, TextAreaField, DecimalField

class CurrencyForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')
    exchange_rate_ks = DecimalField('Kosovo')
    exchange_rate_me = DecimalField('Montenegro')
    exchange_rate_rs = DecimalField('Serbia')

