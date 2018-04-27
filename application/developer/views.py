from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.developer.forms import DeveloperForm
from application.developer.models import Developer
from application.games.models import VideoGame

@app.route("/developers", methods=["GET"])
def developers_index():
    return render_template("developer/list.html", developers=Developer.query.all())

@app.route("/developers/new")
def developer_form():
    return render_template("developer/new.html", form = DeveloperForm())

@app.route("/developers", methods=["POST"])
def developer_create():
    form = DeveloperForm(request.form)

    if not form.validate():
        return render_template("developer.new.html", form = form)

    d = Developer(form.name.data, form.country.data)

    db.session().add(d)
    db.session().commit()

    return redirect(url_for("developers_index"))

@app.route("/developers/<dev_id>", methods=["GET"])
def developer_view(dev_id):
    games = VideoGame.get_by_developer(dev_id)
    developer = Developer.query.get(dev_id)
    return render_template("developer/developer.html", games = games, dev = developer)

@app.route("/developers/<dev_id>", methods=["POST"])
@login_required(role="ADMIN")
def developer_delete(dev_id):
    d = Developer.query.get(dev_id)
    db.session.delete(d)
    db.session.commit()

    return redirect(url_for("developers_index"))