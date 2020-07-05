from flask import Flask, render_template,session, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators = [DataRequired()])
    age = StringField("What is your age?", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        return redirect(url_for('index'))
    form.name.data = ''
    form.age.data = ''
    return render_template('index.html', form=form, name=session.get('name'), age=session.get('age'))


if __name__=='__main__':
    app.run(debug=True)
