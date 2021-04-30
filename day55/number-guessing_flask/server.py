from flask import Flask
import random

app = Flask(__name__)
ran = random.randint(0,9)
@app.route('/')

def guess():
    # ran = random.randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:num>')
def number(num):
    if ran == num:
        return "<h1 style='color: green'>Got correct number</h1>"
    elif ran > num:
        return "<h1 style='color: red'>Too low</h1>"
    else:
        return "<h1 style='color: red'>Too high</h1>"


if __name__ == "__main__":
    app.run(debug=True)