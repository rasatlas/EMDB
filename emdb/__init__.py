from flask import Flask, render_template

app = Flask(__name__)


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
