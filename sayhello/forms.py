from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = SubmitField('Name', validators=[DataRequired(), Length(4, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(4, 200)])
    submit = SubmitField()