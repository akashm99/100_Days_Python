from flask import Flask, render_template
import random
from datetime import datetime
import requests


app = Flask(__name__)

def get_response(name):
    age = requests.get(url=f"https://api.agify.io/?name={name}")
    gender = requests.get(url=f"https://api.genderize.io/?name={name}")
    age = age.json()['age']
    gender = gender.json()['gender'].title()
    return age, gender

@app.route('/')
def home():
    # return 'hello world'
    year = datetime.now().year
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def age_gender(name):
    data = get_response(name)
    age = data[0]
    gender = data[1]
    return render_template('guess.html', name=name.title(), age=age, gender=gender)
    # return f'<h1>age = {data[0]} gender = {data[1]} </h1>'

@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/bc7b160cdb60835cb479")
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)