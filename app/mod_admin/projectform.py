from wtforms import Form, StringField, TextAreaField

class ProjectForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')
