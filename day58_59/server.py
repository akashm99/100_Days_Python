from flask import Flask
from flask import render_template
import requests

response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9")
posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
