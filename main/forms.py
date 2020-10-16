from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    link = StringField('Paste link', validators=[DataRequired()])
    submit = SubmitField('Submit')
