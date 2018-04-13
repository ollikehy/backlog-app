from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.games.models import VideoGame, GameInstance
from application.auth.models import User
from application.games.forms import GameForm, EditForm

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = VideoGame.query.all())

@app.route("/<user_id>/games", methods=["GET"])
def user_games(user_id):
    games = GameInstance.find_games_by_user(user_id)
    return render_template("games/userlist.html", user = User.query.get(user_id), games = games)

@app.route("/<user_id>/games/<game_id>", methods=["POST"])
def user_add_game(user_id, game_id):
    g = GameInstance(user_id, game_id)
    db.session().add(g)
    db.session().commit()
    return redirect(url_for("games_index"))

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
    return render_template("games/edit.html", game = VideoGame.query.get(game_id), form = EditForm())

@app.route("/games/<game_id>", methods=["POST"])
@login_required
def games_update(game_id):
    form = EditForm(request.form)

    if not form.validate():
        return render_template("games/edit.html", game = VideoGame.query.get(game_id), form = form)

    g = VideoGame.query.get(game_id)
    if form.name.data != "":
        g.name = form.name.data
    if form.releaseYear.data != "":
        g.releaseYear = form.releaseYear.data
    if form.genre.data != "":
        g.genre = form.genre.data

    db.session().commit()

    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/delete", methods=["POST"])
@login_required
def game_delete(game_id):
    g = VideoGame.query.get(game_id)
    db.session().delete(g)
    db.session().commit()

    return redirect(url_for("games_index"))