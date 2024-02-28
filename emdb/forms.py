#!/usr/bin/python3
"""A module containing definition of Forms for data input."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import FileField, TextAreaField
from wtforms.validators import DataRequired


class ActorForm(FlaskForm):
    FirstName = StringField("First Name", validators=[DataRequired()])
    FatherName = StringField("Father Name", validators=[DataRequired()])
    GrandFatherName = StringField("Grand Father Name")
    Height = StringField("Height")
    HeadShot = FileField("Head Shot", validators=[DataRequired()])
    BirthDate = DateField("Birth Date")
    DeathDate = DateField("Death Date")
    BtnActor = SubmitField("Save")


class LanguageForm(FlaskForm):
    Language = StringField("Language", validators=[DataRequired()])
    BtnLanguage = SubmitField("Save")


class GenreForm(FlaskForm):
    Genre = StringField("Genre", validators=[DataRequired()])
    BtnGenre = SubmitField("Save")


class PGRatingForm(FlaskForm):
    PGRating = StringField("PG Rating", validators=[DataRequired()])
    BtnPGRating = SubmitField("Save")


class MovieForm(FlaskForm):
    Title = StringField("Title", validators=[DataRequired()])
    Cover = FileField("Cover", validators=[DataRequired()])
    ReleaseDate = DateField("Release Date", validators=[DataRequired()])
    Duration = StringField("Duration", validators=[DataRequired()])
    Synopsis = TextAreaField("Synopsis", validators=[DataRequired()])
    OfficialWebsite = StringField("Website")
    Budget = StringField("Budget")
    BtnMovie = SubmitField("Save")
