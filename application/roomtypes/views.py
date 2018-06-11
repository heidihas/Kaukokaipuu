from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.roomtypes.models import RoomType
from application.roomtypes.forms import RoomTypeForm

@app.route("/roomtypes/new/")
@login_required
def roomtypes_form():
    return render_template("roomtypes/new.html", form = RoomTypeForm())

@app.route("/roomtypes/", methods=["POST"])
def roomtypes_create():
    form = RoomTypeForm(request.form)

    if not form.validate():
        return render_template("roomtypes/new.html", form = form)
        
    r = RoomType(form.name.data, form.size.data, form.price.data)
    r.seaside_view = form.seaside_view.data
    r.air_conditioned = form.air_conditioned.data
    r.mini_bar = form.mini_bar.data
    r.tv = form.tv.data
    r.bath = form.bath.data

    db.session().add(r)
    db.session().commit()
    
    return redirect(url_for("index"))