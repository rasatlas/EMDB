from flask import Flask, render_template
from models.people import People
from models.engine import storageengine
from .forms import ActorForm, Language, Genre, PGRating


app = Flask(__name__)
app.config['SECRET_KEY'] = "dev"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/movies')
@app.route('/movies/')
def movies():
    return render_template("movies.html")


@app.route('/movies/<title>')
def movie(title):
    return render_template("movie.html", title=title)


@app.route('/actors')
@app.route('/actors/')
def actors():
    return render_template("actors.html")


@app.route('/actors/<name>')
def actor(name):
    return render_template("actor.html", name=name)


@app.route('/admin', methods=["GET", "POST"])
def admin():
    form_actorForm = ActorForm()
    form_language = Language()
    form_genre = Genre()
    form_pgrating = PGRating()

    if form_actorForm.validate_on_submit():
        FirstName = form_actorForm.FirstName.data
        form_actorForm.FirstName.data = ''
        FatherName = form_actorForm.FatherName.data
        form_actorForm.FatherName.data = ''
        GrandFatherName = form_actorForm.GrandFatherName.data
        form_actorForm.GrandFatherName.data = ''
        Height = form_actorForm.Height.data
        form_actorForm.Height.data = ''
        HeadShot = form_actorForm.HeadShot.data
        form_actorForm.HeadShot.data = ''
        BirthDate = form_actorForm.BirthDate.data
        form_actorForm.BirthDate.data = ''
        DeathDate = form_actorForm.DeathDate.data
        form_actorForm.DeathDate.data = ''
        record = People(FirstName, FatherName, GrandFatherName, BirthDate,
                        DeathDate, Height, HeadShot)
        storageengine.reload()
        storageengine.new(record)
        storageengine.save()
        storageengine.close()
        return render_template('editor.html', form=form_actorForm)

    if form_language.validate_on_submit():
        return render_template('editor.html', form1=form_language)

    if form_genre.validate_on_submit():
        return render_template('editor.html', form2=form_genre)

    if form_pgrating.validate_on_submit():
        return render_template('editor.html', form3=form_pgrating)

    return render_template('editor.html', form=form_actorForm,
                           form1=form_language, form2=form_genre,
                           form3=form_pgrating)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
