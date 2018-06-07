from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class AccomodationForm(FlaskForm):
    name = StringField("Accomodation name", [validators.Length(min=2), validators.Length(max=20)])
    description = TextAreaField("Description", [validators.Length(max=250)])

    class Meta:
        csrf = False


class AccomodationChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)])
    description = TextAreaField("New description", [validators.Length(max=250)])

    class Meta:
        csrf = False