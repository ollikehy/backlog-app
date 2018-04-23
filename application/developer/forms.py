from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DeveloperForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    country = StringField("Country", [validators.Length(min=1)])

    class Meta:
        csrf = False