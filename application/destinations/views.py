from application import app, db
from flask import redirect, render_template, request, url_for
from application.destinations.models import Destination

@app.route("/destinations", methods=["GET"])
def destinations_index():
    return render_template("destinations/list.html", destinations = Destination.query.all())

@app.route("/destinations/new/")
def destinations_form():
    return render_template("destinations/new.html")

@app.route("/destinations/", methods=["POST"])
def destinations_create():
    d = Destination(request.form.get("name"), request.form.get("description"))
    
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("destinations_index"))
