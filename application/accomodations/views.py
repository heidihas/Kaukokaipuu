from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.destinations.models import Destination
from application.roomtypes.models import RoomType
from application.likes.models import LikeAccomodation
from application.likes.models import LikeDestination
from application.accomodations.models import Accomodation
from application.accomodations.forms import AccomodationForm
from application.accomodations.forms import AccomodationChangeForm

@app.route("/destinations/<destination_id>/accomodations/new/")
@login_required(role="ADMIN")
def accomodations_form(destination_id):
    return render_template("accomodations/new.html", destination = Destination.query.get(destination_id), form = AccomodationForm())

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/", methods=["GET"])
def accomodations_one(destination_id, accomodation_id):
    like = 0
    if current_user.is_authenticated:
        if LikeAccomodation.has_liked(current_user.id, accomodation_id):
            like = LikeAccomodation.has_liked(current_user.id, accomodation_id)
    return render_template("accomodations/accomodation.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id), likes = LikeAccomodation.how_many_likes_accomodation(accomodation_id), roomtypes = Accomodation.children_in_order(accomodation_id), user = current_user, liked = like, bookings = Accomodation.how_many_bookings(accomodation_id))

@app.route("/accomodations/<accomodation_id>/change/", methods=["GET"])
@login_required(role="ADMIN")
def accomodations_one_change(accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    return render_template("accomodations/change.html", accomodation = a, form = AccomodationChangeForm(name=a.name, description=a.description, pricelevel=a.pricelevel, pool=a.pool, spa=a.spa, gym=a.gym, restaurant=a.restaurant))

@app.route("/accomodations/<accomodation_id>/roomtypes/", methods=["GET"])
@login_required(role="ADMIN")
def accomodations_roomtypes(accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    return render_template("roomtypes/list.html", accomodation = a, roomtypes = RoomType.remaining_roomtypes(accomodation_id))

@app.route("/destinations/<destination_id>/accomodations/search/", methods=["POST"])
def accomodations_search(destination_id):
    accomodation = Accomodation.query.filter(Accomodation.name.ilike(request.form.get("search"))).first()
    if not accomodation:
        like = 0
        if current_user.is_authenticated:
            if LikeDestination.has_liked(current_user.id, destination_id):
                like = LikeDestination.has_liked(current_user.id, destination_id)
                
        return render_template("destinations/destination.html", destination = Destination.query.get(destination_id), likes = LikeDestination.how_many_likes_destination(destination_id), accomodations = Accomodation.accomodations_in_order(destination_id), user = current_user, liked = like, bookings = Destination.how_many_bookings(destination_id), error = "No results were found")
    
    return redirect(url_for("accomodations_one", destination_id=accomodation.destination_id, accomodation_id=accomodation.id))

@app.route("/destinations/<destination_id>/accomodations/", methods=["POST"])
@login_required(role="ADMIN")
def accomodations_create(destination_id):
    form = AccomodationForm(request.form)

    accomodation = Accomodation.query.filter_by(name=form.name.data).first()
    if accomodation:
        return render_template("accomodations/new.html", destination = Destination.query.get(destination_id), form = form, error = "Accomodation already exists")
     
    if not form.validate():
        return render_template("accomodations/new.html", destination = Destination.query.get(destination_id), form = form)

    a = Accomodation(form.name.data, form.description.data, form.pricelevel.data, destination_id)
    a.pool = form.pool.data
    a.spa = form.spa.data
    a.gym = form.gym.data
    a.restaurant = form.restaurant.data
    
    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=a.destination_id))

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/", methods=["POST"])
@login_required(role="ADMIN")
def accomodations_delete(destination_id, accomodation_id):
    Accomodation.delete_roomtypes_linked(accomodation_id)
    LikeAccomodation.query.filter_by(accomodation_id=accomodation_id).delete()
    Accomodation.query.filter_by(id=accomodation_id).delete()
    db.session().commit()
    
    return redirect(url_for("destinations_one", destination_id=destination_id))

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/unavailable/", methods=["POST"])
@login_required(role="ADMIN")
def accomodations_unavailable(destination_id, accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    a.unavailable = True

    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/available/", methods=["POST"])
@login_required(role="ADMIN")
def accomodations_available(destination_id, accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    a.unavailable = False

    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))

@app.route("/accomodations/<accomodation_id>/change/", methods=["POST"])
@login_required(role="ADMIN")
def accomodations_change(accomodation_id):
    form = AccomodationChangeForm(request.form)

    if not form.validate():
        return render_template("accomodations/change.html", accomodation = Accomodation.query.get(accomodation_id), form = form)

    a = Accomodation.query.get(accomodation_id)
    a.name = form.name.data
    a.description = form.description.data
    a.pricelevel = form.pricelevel.data
    a.pool = form.pool.data
    a.spa = form.spa.data
    a.gym = form.gym.data
    a.restaurant = form.restaurant.data
    
    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))

@app.route("/accomodations/<accomodation_id>/like/", methods=["POST"])
@login_required(role="CLIENT")
def accomodations_like(accomodation_id):

    a = Accomodation.query.get(accomodation_id)
    c = current_user

    l = LikeAccomodation(c.id, a.id)
    
    db.session().add(l)
    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))
