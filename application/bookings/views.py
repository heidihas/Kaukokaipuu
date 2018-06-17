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
    return render_template("bookings/list.html", how_many_bookings=Client.how_many_bookings(), all_bookings=Booking.all_bookings())

@app.route("/<destination_id>/accomodations/<accomodation_id>/bookings/new/<roomtype_id>/")
@login_required(role="CLIENT")
def bookings_form(destination_id, accomodation_id, roomtype_id):
    return render_template("bookings/new.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id), roomtype = RoomType.query.get(roomtype_id), form = BookingForm())

@app.route("/<destination_id>/accomodations/<accomodation_id>/bookings/new/<roomtype_id>/", methods=["POST"])
@login_required(role="CLIENT")
def bookings_create(destination_id, accomodation_id, roomtype_id):
    form = BookingForm(request.form)
    
    if not (form.email_notification.data or form.phone_notification.data):
        return render_template("bookings/new.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id), roomtype = RoomType.query.get(roomtype_id), form = BookingForm(), error = "Choose at least one of the two.")

    x = random.choice(range(1000000, 9999999))
    
    bookings = Booking.booking_number_exists(x)
    while not bookings:
        x = random.choice(range(1000000, 9999999))
        bookings = Booking.booking_number_exists(x)

    b = Booking(x, roomtype_id, accomodation_id)
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