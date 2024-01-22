from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

class PlaceOrderForm(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), email()])
    address = StringField("Address", validators=[InputRequired()])    
    submit = SubmitField("Place Order")