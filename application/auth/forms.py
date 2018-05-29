from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class ClientForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2), validators.Length(max=144)])
    username = StringField("Username", [validators.Length(min=2), validators.Length(max=20)])
    password = PasswordField("Password", [validators.Length(min=7), validators.Length(max=10)])

    class Meta:
        csrf = False