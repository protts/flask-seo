from wtforms import Form, StringField, validators


class DomainForm(Form):
	domain = StringField('Username', [validators.Length(min=1, max=999)])