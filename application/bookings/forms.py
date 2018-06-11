from flask_wtf import FlaskForm
from wtforms import BooleanField

class BookingForm(FlaskForm):
    
    email_notification = BooleanField("Email", render_kw={"class":"form-control"})
    phone_notification = BooleanField("Phone", render_kw={"class":"form-control"})

    class Meta:
        csrf = False