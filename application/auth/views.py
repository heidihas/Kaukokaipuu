from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Client
from application.auth.forms import LoginForm
from application.auth.forms import ClientForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    client = Client.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not client:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(client)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/client/new/")
def client_form():
    return render_template("auth/new.html", form = ClientForm())

@app.route("/client/", methods=["POST"])
def client_create():
    form = ClientForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)
        
    d = Client(form.name.data, form.username.data, form.password.data)
    
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("index"))