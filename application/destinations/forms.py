from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class DestinationForm(FlaskForm):
    name = StringField("Destination name", [validators.Length(min=2), validators.Length(max=20)])
    description = StringField("Description", [validators.Length(max=250)])

    class Meta:
        csrf = False

class DestinationDeleteForm(FlaskForm):
    submitDelete = SubmitField("Delete destination")

    class Meta:
        csrf = False

class DestinationChangeNameForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=20)])
    submit1 = SubmitField("Change name")

    class Meta:
        csrf = False

class DestinationChangeDescriptionForm(FlaskForm):
    description = StringField("New description", [validators.Length(max=250)])
    submit2 = SubmitField("Change description")

    class Meta:
        csrf = False