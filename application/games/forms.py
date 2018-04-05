from flask_wtf import FlaskForm
from wtforms import StringField, validators

class GameForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    releaseYear = StringField("Release year", [validators.Length(min=4)])
    genre = StringField("Genre")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Name", [validators.Optional(), validators.Length(min=1)])
    releaseYear = StringField("Release year", [validators.Optional(), validators.length(min=4)])
    genre = StringField("Genre", [validators.Optional()])

    class Meta:
        csrf = False