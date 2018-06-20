from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
import random
from application.auth.models import Client
from application.destinations.models import Destination
from application.accomodations.models import Accomodation
from application.roomtypes.models import RoomType
from application.bookings.models import Booking
from application.bookings.forms import BookingForm

@app.route("/bookings", methods=["GET"])
@login_required(role="ADMIN")
def bookings_index():
    return render_template("bookings/list.html", how_many_bookings = Client.how_many_bookings(), all_bookings = Booking.all_bookings())

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/bookings/new/<roomtype_id>/")
@login_required(role="CLIENT")
def bookings_form(destination_id, accomodation_id, roomtype_id):
    d = Destination.query.get(destination_id)
    a = Accomodation.query.get(accomodation_id)
    r = RoomType.query.get(roomtype_id)
    price = a.pricelevel * r.price
    return render_template("bookings/new.html", destination = d, accomodation = a, roomtype = r, price = price, form = BookingForm())

@app.route("/destinations/<destination_id>/accomodations/<accomodation_id>/bookings/new/<roomtype_id>/", methods=["POST"])
@login_required(role="CLIENT")
def bookings_create(destination_id, accomodation_id, roomtype_id):
    form = BookingForm(request.form)

    d = Destination.query.get(destination_id)
    a = Accomodation.query.get(accomodation_id)
    r = RoomType.query.get(roomtype_id)
    price = a.pricelevel * r.price

    if not form.validate():
        return render_template("bookings/new.html", destination = d, accomodation = a, roomtype = r, price = price, form = form, error = "Choose at least one of the two notification options.")

    if not (form.email_notification.data or form.phone_notification.data):
        return render_template("bookings/new.html", destination = d, accomodation = a, roomtype = r, price = price, form = form, error = "Choose at least one of the two notification options.")

    x = random.choice(range(1000000, 9999999))
    
    bookings = Booking.booking_number_exists(x)
    while not bookings:
        x = random.choice(range(1000000, 9999999))
        bookings = Booking.booking_number_exists(x)

    r = RoomType.query.get(roomtype_id)
    a = Accomodation.query.get(accomodation_id)
    nights = form.nights.data
    price = a.pricelevel * r.price * nights

    b = Booking(x, roomtype_id, price, nights, accomodation_id)
    b.email_notification = form.email_notification.data
    b.phone_notification = form.phone_notification.data
    b.client_id = current_user.id
    
    db.session().add(b)
    db.session().commit()
    
    return redirect(url_for("client_my"))

@app.route("/client/mypage/delete/<booking_id>/", methods=["POST"])
@login_required(role="CLIENT")
def bookings_delete(booking_id):

    Booking.query.filter_by(id=booking_id).delete()
    db.session().commit()

    return render_template("auth/my.html", client = current_user, approved_bookings = Booking.approved_bookings(current_user.id, True), not_approved_bookings = Booking.approved_bookings(current_user.id, False))

@app.route("/bookings/<booking_id>/", methods=["POST"])
@login_required(role="ADMIN")
def bookings_set_approved(booking_id):

    b = Booking.query.get(booking_id)
    b.approved = True
    
    db.session().commit()

    return redirect(url_for("bookings_index"))