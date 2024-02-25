from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FileField
from wtforms.validators import DataRequired


class ActorForm(FlaskForm):
    FirstName = StringField("First Name", validators=[DataRequired()])
    FatherName = StringField("Father Name", validators=[DataRequired()])
    GrandFatherName = StringField("Grand Father Name")
    Height = StringField("Height")
    HeadShot = FileField("Head Shot", validators=[DataRequired()])
    BirthDate = DateField("Birth Date")
    DeathDate = DateField("Death Date")
    Submit = SubmitField("Save")


class Language(FlaskForm):
    Language = StringField("Language", validators=[DataRequired()])
    Submit = SubmitField("Save")


class Genre(FlaskForm):
    Genre = StringField("Genre", validators=[DataRequired()])
    Submit = SubmitField("Save")


class PGRating(FlaskForm):
    PGRating = StringField("PG Rating", validators=[DataRequired()])
    Submit = SubmitField("Save")
