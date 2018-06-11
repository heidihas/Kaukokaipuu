from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class RoomTypeForm(FlaskForm):
    name = StringField("Room-type name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    size = IntegerField("Size", [validators.NumberRange(message='Value should be between 1 and 6.', min=1, max=6)], render_kw={"class":"form-control"})
    price = IntegerField("Price", [validators.NumberRange(message='Value should be between 1 and 1000.')], render_kw={"class":"form-control"})

    seaside_view = BooleanField("Seaside view", render_kw={"class":"form-control"})
    air_conditioned = BooleanField("Air-conditioned", render_kw={"class":"form-control"})
    mini_bar = BooleanField("Mini-bar", render_kw={"class":"form-control"})
    tv = BooleanField("Tv", render_kw={"class":"form-control"})
    bath = BooleanField("Bath", render_kw={"class":"form-control"})

    class Meta:
        csrf = False