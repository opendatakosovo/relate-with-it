from wtforms import Form, StringField, TextAreaField

class CurrencyForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')
    conversion_rate = StringField('Conversion rate')


