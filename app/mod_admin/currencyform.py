from wtforms import Form, StringField, TextAreaField, DecimalField

class CurrencyForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')
    value_ks = DecimalField('Kosovo')
    value_me = DecimalField('Montenegro')
    value_rs = DecimalField('Serbia')

