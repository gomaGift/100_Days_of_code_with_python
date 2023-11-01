from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, InputRequired


class Forms(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password', validators=[InputRequired('enter password ')])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = 'withkindofcodingklfdkwmo,,fkssklall__'
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    fo = Forms()
    if fo.validate_on_submit():
        if fo.email.data == 'admin@gmail.com' and fo.password.data == '1234566':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=fo)


if __name__ == '__main__':
    app.run(debug=True)
