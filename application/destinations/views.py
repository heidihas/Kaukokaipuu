from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.destinations.models import Destination
from application.destinations.forms import DestinationForm

@app.route("/destinations", methods=["GET"])
def destinations_index():
    return render_template("destinations/list.html", destinations = Destination.query.all())

@app.route("/destinations/new/")
@login_required
def destinations_form():
    return render_template("destinations/new.html", form = DestinationForm())

@app.route("/destinations/<destination_id>/", methods=["GET"])
def destinations_one(destination_id):
    return render_template("destinations/destination.html", destination = Destination.query.get(destination_id))

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
def destinations_changename(destination_id):
    d = Destination.query.get(destination_id)
    d.name = request.form.get("name")
    
    db.session().commit()
    
    return redirect(url_for("destinations_index"))


@app.route("/destinations/<destination_id>/", methods=["POST"])
@login_required
def destinations_changedescription(destination_id):
    d = Destination.query.get(destination_id)
    d.description = request.form.get("description")
    
    db.session().commit()
    
    return redirect(url_for("destinations_index"))


@app.route("/destinations/<destination_id>/", methods=["POST"])
@login_required
def destinations_delete(destination_id):
    Destination.query.filter_by(id=destination_id).delete()
    db.session().commit()
    
    return redirect(url_for("destinations_index"))