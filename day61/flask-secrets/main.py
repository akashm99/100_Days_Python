from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c21465221d58bcacf79f30d8cee9f55a'
Bootstrap(app)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log in')


@app.route("/")
def home():
    return render_template('index.html')



@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
            # print(form.email.data)
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)