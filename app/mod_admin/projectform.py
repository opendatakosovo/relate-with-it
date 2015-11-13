from wtforms import Form, StringField, TextAreaField, FloatField, SelectField

class ProjectForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')
    cost = FloatField('Cost')
    source_type = SelectField('Source type',
        choices=[('', ''), ('Link', 'Link (URL)'), ('Open Data', 'Open Data')])
    source_ref = StringField('Source reference')
