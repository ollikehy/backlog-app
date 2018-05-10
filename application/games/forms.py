from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, validators

from application import db
from sqlalchemy.sql import text
from application.developer.models import Developer

class GameForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    releaseyear = SelectField("Release year", choices=[(str(i), i) for i in reversed(range(1950, 2018))])
    genre = SelectField("Genre", choices=[('Action','Action'),('Adventure','Adventure'),
    ('Fighter','Fighter'),('Indie','Indie'),('Music','Music'),('Other','Other'),('Puzzle','Puzzle'),
    ('RPG','RPG'),('Shooter','Shooter'),('Simulation','Simulation'),('Sports','Sports')])
    developer = SelectField("Developer")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Name", [validators.Optional(), validators.Length(min=1)])
    releaseyear = StringField("Release year", [validators.Optional(), validators.length(min=4)])
    genre = SelectField("Genre", choices=[('Action','Action'),('Adventure','Adventure'),
    ('Fighter','Fighter'),('Indie','Indie'),('Music','Music'),('Other','Other'),('Puzzle','Puzzle'),
    ('RPG','RPG'),('Shooter','Shooter'),('Simulation','Simulation'),('Sports','Sports')])
    developer = SelectField("Developer")

    class Meta:
        csrf = False