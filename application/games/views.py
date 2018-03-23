from application import app, db
from flask import redirect, render_template, request, url_for
from application.games.models import VideoGame

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = VideoGame.query.all())

@app.route("/games/new/")
def games_form():
    return render_template("games/new.html")

@app.route("/games/", methods=["POST"])
def games_create():
    g = VideoGame(request.form.get("name"), request.form.get("releaseYear"), request.form.get("genre"))

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>", methods=["GET"])
def games_edit(game_id):
    return render_template("games/edit.html", game = VideoGame.query.get(game_id))

@app.route("/games/<game_id>", methods=["POST"])
def games_update(game_id):
    if (not request.form.get("name") or not request.form.get("year") or not request.form.get("genre")):
        return redirect(url_for("error_page"))
    
    g = VideoGame.query.get(game_id)
    g.name = request.form.get("name")
    g.releaseYear = request.form.get("year")
    g.genre = request.form.get("genre")

    db.session().commit()

    return redirect(url_for("games_index"))

@app.route("/error")
def error_page():
    return render_template("error.html")