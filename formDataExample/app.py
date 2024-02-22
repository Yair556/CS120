'''
Simple Flask Form Example, No Flask-WTF
'''

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         print(request.form)
#         name = request.form['name']
#         return f'Hello, {name}!'
#     else:
#         return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

'''
Simple Flask Form Example, With Flask-WTF
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = 'public'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'private'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
app.testing = True

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return f'Hello, {name}!'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)