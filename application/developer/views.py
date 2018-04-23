from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.developer.forms import DeveloperForm
from application.developer.models import Developer

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