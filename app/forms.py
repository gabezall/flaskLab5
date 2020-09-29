from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewArtistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')