from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    submit = SubmitField('Enviar')