from wtforms import Form, StringField, TextAreaField, FloatField, SelectField

class ProjectForm(Form):

    # The region where the project applies
    region = SelectField('Region',
        choices=[('', ''), ('Kosovo', 'Kosovo'), ('Montenegro', 'Montenegro'), ('Serbia', 'Serbia')])

    # Name of the project.
    name = StringField('Name')

    # A description if the project.
    description = TextAreaField('Description')

    # The cost of the project.
    cost = FloatField('Cost')

    currency = SelectField('Currency',
        choices=[('', ''), ('EUR', 'Euro'), ('RSD', 'Serbian Dinar')])

    # The data source.
    source_type = SelectField('Source type',
        choices=[('', ''), ('Link', 'Link (URL)'), ('Open Data', 'Open Data')])

    # Reference to the source
    source_ref = StringField('Source reference')
