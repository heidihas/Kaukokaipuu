from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, validators

class AccomodationForm(FlaskForm):
    name = StringField("Accomodation name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    description = TextAreaField("Description", [validators.Length(max=250)], render_kw={"class":"form-control"})

    pool = BooleanField("Pool", render_kw={"class":"form-control"})
    spa = BooleanField("Spa", render_kw={"class":"form-control"})
    gym = BooleanField("Gym", render_kw={"class":"form-control"})
    restaurant = BooleanField("Restaurant", render_kw={"class":"form-control"})

    class Meta:
        csrf = False


class AccomodationChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    description = TextAreaField("New description", [validators.Length(max=250)], render_kw={"class":"form-control"})

    pool = BooleanField("Pool", render_kw={"class":"form-control"})
    spa = BooleanField("Spa", render_kw={"class":"form-control"})
    gym = BooleanField("Gym", render_kw={"class":"form-control"})
    restaurant = BooleanField("Restaurant", render_kw={"class":"form-control"})
    
    class Meta:
        csrf = False