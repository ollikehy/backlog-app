from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class GameForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    releaseyear = StringField("Release year", [validators.Length(min=4)])
    genre = SelectField("Genre", choices=[('Action','Action'),('Adventure','Adventure'),
    ('Fighter','Fighter'),('Indie','Indie'),('Music','Music'),('Other','Other'),('Puzzle','Puzzle'),
    ('RPG','RPG'),('Shooter','Shooter'),('Simulation','Simulation'),('Sports','Sports')])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Name", [validators.Optional(), validators.Length(min=1)])
    releaseyear = StringField("Release year", [validators.Optional(), validators.length(min=4)])
    genre = SelectField("Genre", choices=[('Action','Action'),('Adventure','Adventure'),
    ('Fighter','Fighter'),('Indie','Indie'),('Music','Music'),('Other','Other'),('Puzzle','Puzzle'),
    ('RPG','RPG'),('Shooter','Shooter'),('Simulation','Simulation'),('Sports','Sports')])

    class Meta:
        csrf = False