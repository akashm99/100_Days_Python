from flask import Flask
from flask import render_template, request
import requests
import smtplib

OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9")
posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        try:
            send_email(data["username"], data["useremail"], data["usercontact"], data["usermessage"])
        except:
            return render_template("contact.html", msg_sent=False)
        else:
            return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


# @app.route("/form-entry", methods=["POST"])
# def recieve_data():
#     details = {
#         'name': request.form['username'],
#         'email': request.form['useremail'],
#         'contact': request.form['usercontact'],
#         'message': request.form['usermessage'],
#     }
#     return f"{details}"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
