from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class DestinationForm(FlaskForm):
    name = StringField("Destination name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    description = TextAreaField("Description", [validators.Length(max=250)], render_kw={"class":"form-control"})

    class Meta:
        csrf = False

class DestinationChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    description = TextAreaField("New description", [validators.Length(max=250)], render_kw={"class":"form-control"})

    class Meta:
        csrf = False