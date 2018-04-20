from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.games.models import VideoGame, GameInstance
from application.auth.models import User
from application.games.forms import GameForm, EditForm

@app.route("/games", methods=["GET"])
def games_index():
    usergames = []
    if current_user.is_authenticated:
        ug = GameInstance.find_games_by_user(current_user.id)
        for game in ug:
            usergames.append(game['name'])
    return render_template("games/list.html", games = VideoGame.query.all(), usergames = usergames)

@app.route("/<user_id>/games", methods=["GET"])
@login_required()
def user_games(user_id):
    games = GameInstance.find_games_by_user(user_id)
    return render_template("games/userlist.html", user = User.query.get(user_id), games = games)

@app.route("/<user_id>/games/<game_id>", methods=["POST"])
@login_required()
def user_add_game(user_id, game_id):
    g = GameInstance(user_id, game_id)
    db.session().add(g)
    db.session().commit()
    return redirect(url_for("games_index"))

@app.route("/<user_id>/games/<game_id>/delete", methods=["POST"])
@login_required()
def user_delete_game(user_id, game_id):
    GameInstance.delete_games_by_user(user_id, game_id)

    return redirect(url_for("user_games", user_id=user_id))

@app.route("/games/new/")
@login_required()
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/", methods=["POST"])
@login_required()
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template("games/new.html", form = form)

    g = VideoGame(form.name.data, form.releaseyear.data, form.genre.data)

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))


@app.route("/games/<game_id>", methods=["GET"])
def game_view(game_id):
    return render_template("games/game.html", game = VideoGame.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["GET"])
@login_required(role="ADMIN")
def games_edit(game_id):
    return render_template("games/edit.html", game = VideoGame.query.get(game_id), form = EditForm())

@app.route("/games/<game_id>", methods=["POST"])
@login_required()
def games_update(game_id):
    form = EditForm(request.form)

    if not form.validate():
        return render_template("games/edit.html", game = VideoGame.query.get(game_id), form = form)

    g = VideoGame.query.get(game_id)
    if form.name.data != "":
        g.name = form.name.data
    if form.releaseyear.data != "":
        g.releaseyear = form.releaseyear.data
    if form.genre.data != "":
        g.genre = form.genre.data

    db.session().commit()

    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def game_delete(game_id):
    g = VideoGame.query.get(game_id)
    db.session().delete(g)
    db.session().commit()

    return redirect(url_for("games_index"))