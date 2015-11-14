from wtforms import Form, StringField, TextAreaField, DecimalField

class CurrencyForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')

    value_ks = DecimalField('Kosovo')
    source_ks = StringField('Source (Kosovo)')

    value_me = DecimalField('Montenegro')
    source_me = StringField('Source (Montenegro)')

    value_rs = DecimalField('Serbia')
    source_rs = StringField('Source (Serbia)')

