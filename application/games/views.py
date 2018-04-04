from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.games.models import VideoGame
from application.games.forms import GameForm

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = VideoGame.query.all())

@app.route("/games/new/")
@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/", methods=["POST"])
@login_required
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template("games/new.html", form = form)

    g = VideoGame(form.name.data, form.releaseYear.data, form.genre.data)

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))


@app.route("/games/<game_id>", methods=["GET"])
def game_view(game_id):
    return render_template("games/game.html", game = VideoGame.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["GET"])
@login_required
def games_edit(game_id):
    return render_template("games/edit.html", game = VideoGame.query.get(game_id), form = GameForm())

@app.route("/games/<game_id>", methods=["POST"])
@login_required
def games_update(game_id):
    form = GameForm(request.form)

    if not form.validate():
        return render_template("games/list.html", error = "Invalid data, please try again")

    g = VideoGame.query.get(game_id)
    g.name = form.name.data
    g.releaseYear = form.releaseYear.data
    g.genre = form.genre.data

    db.session().commit()

    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/delete", methods=["POST"])
def game_delete(game_id):
    g = VideoGame.query.get(game_id)
    db.session().delete(g)
    db.session().commit()

    return redirect(url_for("games_index"))