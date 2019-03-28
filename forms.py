from flask_wtf import FlaskForm
from wtforms import validators, TextField,SubmitField
from wtforms.fields.html5 import EmailField


class opened_me_form(FlaskForm):
    email = EmailField('email', [validators.DataRequired(), validators.Email()])
    link = TextField("link", [validators.DataRequired()])
    submit = SubmitField("submit")

