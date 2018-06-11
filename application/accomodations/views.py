from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.destinations.models import Destination
from application.accomodations.models import Accomodation
from application.accomodations.forms import AccomodationForm
from application.accomodations.forms import AccomodationChangeForm

@app.route("/<destination_id>/accomodations/new/")
@login_required
def accomodations_form(destination_id):
    return render_template("accomodations/new.html", destination = Destination.query.get(destination_id), form = AccomodationForm())

@app.route("/<destination_id>/accomodations/<accomodation_id>/", methods=["GET"])
def accomodations_one(destination_id, accomodation_id):
    return render_template("accomodations/accomodation.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id))

@app.route("/accomodations/<accomodation_id>/change/", methods=["GET"])
def accomodations_one_change(accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    return render_template("accomodations/change.html", accomodation = a, form = AccomodationChangeForm(name=a.name, description=a.description, pool=a.pool, spa=a.spa, gym=a.gym, restaurant=a.restaurant))

@app.route("/<destination_id>/accomodations/", methods=["POST"])
def accomodations_create(destination_id):
    form = AccomodationForm(request.form)

    if not form.validate():
        return render_template("accomodations/new.html", destination = Destination.query.get(destination_id), form = form)
        
    a = Accomodation(form.name.data, form.description.data, destination_id)
    a.pool = form.pool.data
    a.spa = form.spa.data
    a.gym = form.gym.data
    a.restaurant = form.restaurant.data
    
    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=a.destination_id))

@app.route("/<destination_id>/accomodations/<accomodation_id>/", methods=["POST"])
@login_required
def accomodations_delete(destination_id, accomodation_id):
    Accomodation.query.filter_by(id=accomodation_id).delete()
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=destination_id))

@app.route("/accomodations/<accomodation_id>/change/", methods=["POST"])
@login_required
def accomodations_change(accomodation_id):
    form = AccomodationChangeForm(request.form)

    if not form.validate():
        return render_template("accomodations/change.html", accomodation = Accomodation.query.get(accomodation_id), form = form)

    a = Accomodation.query.get(accomodation_id)
    a.name = form.name.data
    a.description = form.description.data
    a.pool = form.pool.data
    a.spa = form.spa.data
    a.gym = form.gym.data
    a.restaurant = form.restaurant.data
    
    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))
