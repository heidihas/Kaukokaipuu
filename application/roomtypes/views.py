from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.roomtypes.models import RoomType
from application.roomtypes.forms import RoomTypeForm
from application.roomtypes.forms import RoomTypeChangeForm
from application.accomodations.models import Accomodation

@app.route("/roomtypes/new/")
@login_required(role="ADMIN")
def roomtypes_form():
    return render_template("roomtypes/new.html", form = RoomTypeForm())

@app.route("/roomtypes/<roomtype_id>/", methods=["GET"])
@login_required(role="ADMIN")
def roomtypes_one(roomtype_id):
    return render_template("roomtypes/roomtype.html", roomtype = RoomType.query.get(roomtype_id), accomodations = RoomType.query.get(roomtype_id).parents)

@app.route("/roomtypes/<roomtype_id>/change/", methods=["GET"])
@login_required(role="ADMIN")
def roomtypes_one_change(roomtype_id):
    r = RoomType.query.get(roomtype_id)
    return render_template("roomtypes/change.html", roomtype = r, form = RoomTypeChangeForm(name=r.name, size=r.size, price=r.price, seaside_view=r.seaside_view, air_conditioned=r.air_conditioned, mini_bar=r.mini_bar, tv=r.tv, bath=r.bath))

@app.route("/roomtypes/", methods=["POST"])
@login_required(role="ADMIN")
def roomtypes_create():
    form = RoomTypeForm(request.form)

    if not form.validate():
        return render_template("roomtypes/new.html", form = form)
        
    r = RoomType(form.name.data, form.size.data, form.price.data, form.many.data)
    r.seaside_view = form.seaside_view.data
    r.air_conditioned = form.air_conditioned.data
    r.mini_bar = form.mini_bar.data
    r.tv = form.tv.data
    r.bath = form.bath.data

    db.session().add(r)
    db.session().commit()
    
    return redirect(url_for("navigation"))

@app.route("/accomodations/<accomodation_id>/roomtypes/<roomtype_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def roomtypes_delete_one(accomodation_id, roomtype_id):
    a = Accomodation.query.get(accomodation_id)
    Accomodation.delete_roomtypes_one(accomodation_id, roomtype_id)

    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=a.destination_id, accomodation_id=a.id))

@app.route("/roomtypes/<roomtype_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def roomtypes_delete(roomtype_id):
    RoomType.delete_accomodations_linked(roomtype_id)
    RoomType.query.filter_by(id=roomtype_id).delete()
    db.session().commit()
    
    return redirect(url_for("navigation"))

@app.route("/roomtypes/<roomtype_id>/change/", methods=["POST"])
@login_required(role="ADMIN")
def roomtypes_change(roomtype_id):
    form = RoomTypeChangeForm(request.form)

    if not form.validate():
        return render_template("roomtypes/change.html", roomtype = RoomType.query.get(roomtype_id), form = form)

    r = RoomType.query.get(roomtype_id)
    r.name = form.name.data
    r.size = form.size.data
    r.price = form.price.data
    r.many = form.many.data
    r.seaside_view = form.seaside_view.data
    r.air_conditioned = form.air_conditioned.data
    r.mini_bar = form.mini_bar.data
    r.tv = form.tv.data
    r.bath = form.bath.data
    
    db.session().commit()
    
    return redirect(url_for("roomtypes_one", roomtype_id=r.id))

@app.route("/accomodations/<accomodation_id>/roomtypes/<roomtype_id>/", methods=["POST"])
@login_required(role="ADMIN")
def roomtypes_add(roomtype_id, accomodation_id):
    a = Accomodation.query.get(accomodation_id)
    r = RoomType.query.get(roomtype_id)
    a.children.append(r)

    db.session().commit()
    
    return redirect(url_for("accomodations_roomtypes", accomodation_id=accomodation_id))
