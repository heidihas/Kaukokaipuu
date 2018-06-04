from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators

class DestinationForm(FlaskForm):
    name = StringField("Destination name", [validators.Length(min=2), validators.Length(max=20)])
    description = TextAreaField("Description", [validators.Length(max=250)])

    class Meta:
        csrf = False

class DestinationDeleteForm(FlaskForm):
    submitDelete = SubmitField("Delete destination")

    class Meta:
        csrf = False

class DestinationChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)])
    description = TextAreaField("New description", [validators.Length(max=250)])
    submitChange = SubmitField("Change")

    class Meta:
        csrf = False