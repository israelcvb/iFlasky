from flask import Flask, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Eu e a Mucura na canoa!'

bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
