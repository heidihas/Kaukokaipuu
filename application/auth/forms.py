from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class ClientForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2), validators.Length(max=144)], render_kw={"class":"form-control"})
    address = StringField("Address", [validators.Length(min=2), validators.Length(max=144)], render_kw={"class":"form-control"})
    country = StringField("Country", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    email = StringField("Email", [validators.Length(min=2), validators.Length(max=30)], render_kw={"class":"form-control"})
    phone = StringField("Phone", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    username = StringField("Username", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    password = PasswordField("Password", [validators.Length(min=7), validators.Length(max=10)], render_kw={"class":"form-control"})

    class Meta:
        csrf = False

class ClientChangeForm(FlaskForm):
    name = StringField("New name", [validators.Length(min=2), validators.Length(max=144)], render_kw={"class":"form-control"})
    address = StringField("New address", [validators.Length(min=2), validators.Length(max=144)], render_kw={"class":"form-control"})
    country = StringField("New country", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    email = StringField("New email", [validators.Length(min=2), validators.Length(max=30)], render_kw={"class":"form-control"})
    phone = StringField("New phone", [validators.Length(min=2), validators.Length(max=20)], render_kw={"class":"form-control"})
    
    class Meta:
        csrf = False

class PasswordChangeForm(FlaskForm):
    password = PasswordField("Current password", [validators.Length(min=7), validators.Length(max=10)], render_kw={"class":"form-control"})
    new = PasswordField("New password", [validators.Length(min=7), validators.Length(max=10)], render_kw={"class":"form-control"})
    
    class Meta:
        csrf = False