from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.auth.models import Client
from application.destinations.models import Destination
from application.accomodations.models import Accomodation
from application.bookings.models import Booking
from application.bookings.forms import BookingForm

@app.route("/bookings", methods=["GET"])
@login_required
def bookings_index():
    return render_template("bookings/list.html", how_many_bookings=Client.how_many_bookings(), all_bookings=Booking.all_bookings())

@app.route("/<destination_id>/accomodations/<accomodation_id>/bookings/new/")
@login_required
def bookings_form(destination_id, accomodation_id):
    return render_template("bookings/new.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id), form = BookingForm())

@app.route("/<destination_id>/accomodations/<accomodation_id>/bookings/", methods=["POST"])
def bookings_create(destination_id, accomodation_id):
    form = BookingForm(request.form)
    
    if not (form.email_notification.data or form.phone_notification.data):
        return render_template("bookings/new.html", destination = Destination.query.get(destination_id), accomodation = Accomodation.query.get(accomodation_id), form = BookingForm(), error = "Choose at least one of the two.")

    b = Booking(accomodation_id)
    b.email_notification = form.email_notification.data
    b.phone_notification = form.phone_notification.data
    b.client_id = current_user.id
    
    db.session().add(b)
    db.session().commit()
    
    return redirect(url_for("accomodations_one", destination_id=Accomodation.query.get(b.accomodation_id).destination_id, accomodation_id=b.accomodation_id))

@app.route("/client/mypage/delete/<booking_id>/", methods=["POST"])
def bookings_delete(booking_id):

    Booking.query.filter_by(id=booking_id).delete()
    db.session().commit()

    return render_template("auth/my.html", client = current_user, approved_bookings = Booking.approved_bookings(current_user.id, 1), not_approved_bookings = Booking.approved_bookings(current_user.id, 0))

@app.route("/bookings/<booking_id>/", methods=["POST"])
def bookings_set_approved(booking_id):

    b = Booking.query.get(booking_id)
    b.approved = True
    
    db.session().commit()

    return redirect(url_for("bookings_index"))