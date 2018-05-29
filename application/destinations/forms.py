from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DestinationForm(FlaskForm):
    name = StringField("Destination name", [validators.Length(min=2), validators.Length(max=20)])
    description = StringField("Description", [validators.Length(max=250)])

    class Meta:
        csrf = False