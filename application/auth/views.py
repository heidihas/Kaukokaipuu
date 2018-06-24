from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import Client
from application.auth.forms import LoginForm
from application.auth.forms import ClientForm
from application.auth.forms import ClientChangeForm
from application.auth.forms import PasswordChangeForm
from application.destinations.models import Destination
from application.accomodations.models import Accomodation
from application.roomtypes.models import RoomType
from application.bookings.models import Booking

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

@app.route("/client/mypage/")
@login_required(role="CLIENT")
def client_my():
    return render_template("auth/my.html", client = current_user, approved_bookings = Booking.approved_bookings(current_user.id, True), not_approved_bookings = Booking.approved_bookings(current_user.id, False))

@app.route("/client/mypage/change/", methods=["GET"])
@login_required(role="CLIENT")
def client_one_change():
    return render_template("auth/change.html", client = current_user, form = ClientChangeForm(name=current_user.name, address=current_user.address, country=current_user.country, email=current_user.email, phone=current_user.phone))

@app.route("/client/mypage/password/change/", methods=["GET"])
@login_required(role="CLIENT")
def client_one_password_change():
    return render_template("auth/passwordchange.html", client = current_user, form = PasswordChangeForm())

@app.route("/navigation")
@login_required(role="ADMIN")
def navigation():
    return render_template("navigation.html", destinations = Destination.destinations_alphabetic(), accomodations = Accomodation.accomodations_alphabetic(), roomtypes = RoomType.roomtypes_alpabetic())

@app.route("/client/", methods=["POST"])
def client_create():
    form = ClientForm(request.form)

    client = Client.query.filter_by(username=form.username.data).first()
    if client:
        return render_template("auth/new.html", form = form, error = "Username not available")
   
    if not form.validate():
        return render_template("auth/new.html", form = form)

    c = Client(form.name.data, form.address.data, form.country.data, form.email.data, form.phone.data, form.username.data, form.password.data)
    
    db.session().add(c)
    try:
        db.session().commit()
    except:
        db.session().rollback()
        raise
    
    return redirect(url_for("auth_login"))

@app.route("/client/mypage/change/", methods=["POST"])
@login_required(role="CLIENT")
def client_change():
    form = ClientChangeForm(request.form)

    if not form.validate():
        return render_template("auth/change.html", client = current_user, form = form)

    c = current_user
    c.name = form.name.data
    c.address = form.address.data
    c.country = form.country.data
    c.email = form.email.data
    c.phone = form.phone.data
    
    try:
        db.session().commit()
    except:
        db.session().rollback()
        raise
    
    return redirect(url_for("client_my"))

@app.route("/client/mypage/password/change/", methods=["POST"])
@login_required(role="CLIENT")
def client_password_change():
    form = PasswordChangeForm(request.form)

    c = current_user

    if c.password != form.password.data:
        return render_template("auth/passwordchange.html", client = c, form = form, error = "Current password incorrect")
    
    if not form.validate():
        return render_template("auth/passwordchange.html", client = current_user, form = form)

    c.password = form.new.data
    
    try:
        db.session().commit()
    except:
        db.session().rollback()
        raise
    
    return redirect(url_for("client_my"))

@app.route("/client/mypage/delete/", methods=["POST"])
@login_required(role="CLIENT")
def client_delete():
    client = current_user

    Booking.query.filter_by(client_id=client.id).delete()
    Client.query.filter_by(id=client.id).delete()
    
    try:
        db.session().commit()
    except:
        db.session().rollback()
        raise

    return redirect(url_for("index"))
