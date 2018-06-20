from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class RoomTypeForm(FlaskForm):
    name = StringField("Room-type name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    size = IntegerField("Person(s)", [validators.NumberRange(message='Value should be between 1 and 6.', min=1, max=6)], render_kw={"class":"form-control"})
    price = IntegerField("Price/night", [validators.NumberRange(message='Value should be between 1 and 1000.', min=1, max=1000)], render_kw={"class":"form-control"})
    many = IntegerField("Rooms/hotel", [validators.NumberRange(message='Value should be at least 1.', min=1)], render_kw={"class":"form-control"})

    seaside_view = BooleanField("Seaside view", render_kw={"class":"form-control"})
    air_conditioned = BooleanField("Air-conditioned", render_kw={"class":"form-control"})
    mini_bar = BooleanField("Mini-bar", render_kw={"class":"form-control"})
    tv = BooleanField("Tv", render_kw={"class":"form-control"})
    bath = BooleanField("Bath", render_kw={"class":"form-control"})

    class Meta:
        csrf = False

class RoomTypeChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    size = IntegerField("New person(s) number", [validators.NumberRange(message='Value should be between 1 and 6.', min=1, max=6)], render_kw={"class":"form-control"})
    price = IntegerField("New price/night", [validators.NumberRange(message='Value should be between 1 and 1000.', min=1, max=1000)], render_kw={"class":"form-control"})
    many = IntegerField("Rooms/hotel", [validators.NumberRange(message='Value should be at least 1.', min=1)], render_kw={"class":"form-control"})

    seaside_view = BooleanField("Seaside view", render_kw={"class":"form-control"})
    air_conditioned = BooleanField("Air-conditioned", render_kw={"class":"form-control"})
    mini_bar = BooleanField("Mini-bar", render_kw={"class":"form-control"})
    tv = BooleanField("Tv", render_kw={"class":"form-control"})
    bath = BooleanField("Bath", render_kw={"class":"form-control"})

    class Meta:
        csrf = False