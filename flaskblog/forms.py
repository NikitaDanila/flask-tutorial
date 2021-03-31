from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed # Let's us upload images and wath kind
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
