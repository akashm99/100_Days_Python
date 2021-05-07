from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
       pass

if __name__ == '__main__':
    app.run(debug=True)