from wtforms import Form, StringField, TextAreaField

class UnitForm(Form):
    name = StringField('Name')
    coversion_rate = StringField('Conversion rate')
    description = TextAreaField('Description')

