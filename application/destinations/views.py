from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.accomodations.models import Accomodation
from application.destinations.models import Destination
from application.destinations.forms import DestinationForm
from application.destinations.forms import DestinationChangeForm

@app.route("/destinations", methods=["GET"])
def destinations_index():
    return render_template("destinations/list.html", destinations = Destination.destinations_in_order())

@app.route("/destinations/new/")
@login_required(role="ADMIN")
def destinations_form():
    return render_template("destinations/new.html", form = DestinationForm())

@app.route("/destinations/<destination_id>/", methods=["GET"])
def destinations_one(destination_id):
    return render_template("destinations/destination.html", destination = Destination.query.get(destination_id), accomodations = Accomodation.accomodations_in_order(destination_id), user = current_user)

@app.route("/destinations/<destination_id>/change/", methods=["GET"])
@login_required(role="ADMIN")
def destinations_one_change(destination_id):
    d = Destination.query.get(destination_id)
    return render_template("destinations/change.html", destination = d, form = DestinationChangeForm(name=d.name, description=d.description))

@app.route("/destinations/", methods=["POST"])
@login_required(role="ADMIN")
def destinations_create():
    form = DestinationForm(request.form)

    if not form.validate():
        return render_template("destinations/new.html", form = form)
        
    d = Destination(form.name.data, form.description.data)
    
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("navigation"))

@app.route("/destinations/<destination_id>/", methods=["POST"])
@login_required(role="ADMIN")
def destinations_delete(destination_id):
    Accomodation.query.filter_by(destination_id=destination_id).delete()
    Destination.query.filter_by(id=destination_id).delete()
    db.session().commit()
    
    return redirect(url_for("navigation"))

@app.route("/destinations/<destination_id>/change/", methods=["POST"])
@login_required(role="ADMIN")
def destinations_change(destination_id):
    form = DestinationChangeForm(request.form)

    if not form.validate():
        return render_template("destinations/change.html", destination = Destination.query.get(destination_id), form = form)

    d = Destination.query.get(destination_id)
    d.name = form.name.data
    d.description = form.description.data
    
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=d.id))

@app.route("/destinations/<destination_id>/like/", methods=["POST"])
@login_required(role="CLIENT")
def destinations_like(destination_id):

    d = Destination.query.get(destination_id)
    d.rating = d.rating + 1
    
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=d.id))

