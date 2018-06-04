from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.destinations.models import Destination
from application.destinations.forms import DestinationForm
from application.destinations.forms import DestinationDeleteForm
from application.destinations.forms import DestinationChangeForm

@app.route("/destinations", methods=["GET"])
def destinations_index():
    return render_template("destinations/list.html", destinations = Destination.query.all())

@app.route("/destinations/new/")
@login_required
def destinations_form():
    return render_template("destinations/new.html", form = DestinationForm())

@app.route("/destinations/<destination_id>/", methods=["GET"])
def destinations_one(destination_id):
    return render_template("destinations/destination.html", destination = Destination.query.get(destination_id), form = DestinationDeleteForm())

@app.route("/destinations/<destination_id>/change/", methods=["GET"])
def destinations_one_change(destination_id):
    d = Destination.query.get(destination_id)
    return render_template("destinations/change.html", destination = d, form = DestinationChangeForm(name=d.name, description=d.description))

@app.route("/destinations/", methods=["POST"])
def destinations_create():
    form = DestinationForm(request.form)

    if not form.validate():
        return render_template("destinations/new.html", form = form)
        
    d = Destination(form.name.data, form.description.data)
    
    db.session().add(d)
    db.session().commit()
    
    return redirect(url_for("destinations_index"))

@app.route("/destinations/<destination_id>/", methods=["POST"])
@login_required
def destinations_delete(destination_id):
    Destination.query.filter_by(id=destination_id).delete()
    db.session().commit()
    
    return redirect(url_for("destinations_index"))

@app.route("/destinations/<destination_id>/change/", methods=["POST"])
@login_required
def destinations_change(destination_id):
    form = DestinationChangeForm(request.form)

    if not form.validate():
        return render_template("destinations/change.html", destination = Destination.query.get(destination_id), form = form)

    d = Destination.query.get(destination_id)
    d.name = form.name.data
    d.description = form.description.data
    
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=d.id))
