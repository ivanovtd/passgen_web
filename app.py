from flask import Flask, request, render_template, session
import passgen
from werkzeug.datastructures import MultiDict

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecretkey!'

CHOISES = ['8', '10', '12', '16', '20']


class ChoiceForm(FlaskForm):
    length = SelectField(u'length', choices=CHOISES)
    is_use_numbers = BooleanField('numbers')
    is_use_letters = BooleanField('letters')
    is_use_capitals = BooleanField('capitals')
    is_use_specials = BooleanField('specials')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ChoiceForm()

    if form.validate_on_submit():
        session['formdata'] = request.form
        password = passgen.generate_password(MultiDict(request.form))
        return render_template('index.html', form=form, password=password)
    return render_template('index.html', form=form)


if __name__=='__main__':
    app.run(debug=True)