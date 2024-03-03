#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, redirect
from .forms import ActorForm, LanguageForm, GenreForm, PGRatingForm, MovieForm
from .models.people import People
from .models.language import Language
from .models.genre import Genre
from .models.pgrating import PgRating
from .models.movie import Movie
from .models import storage
from werkzeug.utils import secure_filename
import uuid as uuid
import os


app = Flask(__name__)


UPLOAD_DIRECTORY_ACTOR = 'emdb/static/imgs/head_shot/'
UPLOAD_DIRECTORY_MOVIE = 'emdb/static/imgs/cover/'

app.config['SECRET_KEY'] = "dev"
app.config['UPLOAD_DIRECTORY_ACTOR'] = UPLOAD_DIRECTORY_ACTOR
app.config['UPLOAD_DIRECTORY_MOVIE'] = UPLOAD_DIRECTORY_MOVIE

ALLOWED_EXTENSIONS = set(['.jpg', '.jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1]


@app.route('/')
def home():
    movies = storage.all(Movie).values()
    actors = storage.all(People).values()
    return render_template("index.html", movies=movies, actors=actors,
                           UPLOAD_DIRECTORY_ACTOR=UPLOAD_DIRECTORY_ACTOR,
                           UPLOAD_DIRECTORY_MOVIE=UPLOAD_DIRECTORY_MOVIE)


@app.route('/movies')
@app.route('/movies/')
def movies():
    movies = storage.all(Movie).values()
    return render_template("movies.html", movies=movies,
                           UPLOAD_DIRECTORY_MOVIE=UPLOAD_DIRECTORY_MOVIE)


@app.route('/movies/<title>')
def movie(title):
    return render_template("movie.html", title=title)


@app.route('/actors')
@app.route('/actors/')
def actors():
    actors = storage.all(People).values()
    return render_template("actors.html", actors=actors,
                           UPLOAD_DIRECTORY_ACTOR=UPLOAD_DIRECTORY_ACTOR)


@app.route('/actors/<name>')
def actor(name):
    return render_template("actor.html", name=name)


@app.route('/admin', methods=["GET", "POST"])
def admin():
    form_actor = ActorForm()
    form_language = LanguageForm()
    form_genre = GenreForm()
    form_pgrating = PGRatingForm()
    form_movie = MovieForm()

    if request.method == "POST" and 'BtnActor' in request.form:
        actor = People()
        actor.first_name = form_actor.FirstName.data
        actor.father_name = form_actor.FatherName.data
        actor.grand_father_name = form_actor.GrandFatherName.data
        actor.height = form_actor.Height.data
        actor.birth_date = form_actor.BirthDate.data
        actor.death_date = form_actor.DeathDate.data

        # Save filename to db & file to 'UPLOAD_DIRECTORY_ACTOR' directory.
        actor.head_shot = form_actor.HeadShot.data
        pic_filename = secure_filename(actor.head_shot.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename

        saver = request.files['HeadShot']
        actor.head_shot = pic_name
        if not os.path.exists(UPLOAD_DIRECTORY_ACTOR):
            os.makedirs(UPLOAD_DIRECTORY_ACTOR)
            saver.save(os.path.join(app.config['UPLOAD_DIRECTORY_ACTOR'],
                                    pic_name))
        else:
            saver.save(os.path.join(app.config['UPLOAD_DIRECTORY_ACTOR'],
                                    pic_name))

        storage.new(actor)
        storage.save()
        storage.close()
        return redirect(url_for("admin"))

    if request.method == "POST" and 'BtnLanguage' in request.form:
        language = Language()
        language.language = form_language.Language.data
        storage.new(language)
        storage.save()
        storage.close()
        return redirect(url_for("admin"))

    if request.method == "POST" and 'BtnGenre' in request.form:
        genre = Genre()
        genre.genre = form_genre.Genre.data
        storage.new(genre)
        storage.save()
        storage.close()
        return redirect(url_for("admin"))

    if request.method == "POST" and 'BtnPGRating' in request.form:
        pgRating = PgRating()
        pgRating.pg_rating = form_pgrating.PGRating.data
        storage.new(pgRating)
        storage.save()
        storage.close()
        return redirect(url_for("admin"))

    if request.method == "POST" and 'BtnMovie' in request.form:
        movie = Movie()
        movie.title = form_movie.Title.data
        movie.duration = form_movie.Duration.data
        movie.release_date = form_movie.ReleaseDate.data
        movie.synopsis = form_movie.Synopsis.data
        movie.official_website = form_movie.OfficialWebsite.data
        movie.budget = form_movie.Budget.data

        # Save filename to db & file to 'UPLOAD_DIRECTORY_MOVIE' directory.
        movie.cover = form_movie.Cover.data
        cover_filename = secure_filename(movie.cover.filename)
        cover_name = str(uuid.uuid1()) + "_" + cover_filename

        saver = request.files['Cover']
        movie.cover = cover_name
        if not os.path.exists(UPLOAD_DIRECTORY_MOVIE):
            os.makedirs(UPLOAD_DIRECTORY_MOVIE)
            saver.save(os.path.join(app.config['UPLOAD_DIRECTORY_MOVIE'],
                                    cover_name))
        else:
            saver.save(os.path.join(app.config['UPLOAD_DIRECTORY_MOVIE'],
                                    cover_name))

        storage.new(movie)
        storage.save()
        storage.close()
        return redirect(url_for("admin"))

    return render_template('editor.html', form=form_actor,
                           form1=form_language, form2=form_genre,
                           form3=form_pgrating, form4=form_movie)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
