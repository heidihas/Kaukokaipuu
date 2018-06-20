from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, validators

class BookingForm(FlaskForm):
    
    nights = IntegerField("Nights", [validators.NumberRange(message='Choose at least one night.', min=1, max=120)], render_kw={"class":"form-control"})
    email_notification = BooleanField("Email", render_kw={"class":"form-control"})
    phone_notification = BooleanField("Phone", render_kw={"class":"form-control"})

    class Meta:
        csrf = False