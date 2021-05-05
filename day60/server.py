from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def login():
    print(request.method)
    name = request.form['username']
    password = request.form['password']
    return f"<h1>Logged in..</h1> {name} {password}"


if __name__ == "__main__":
    app.run(debug=True)