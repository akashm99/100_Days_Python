from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# import logging
from werkzeug.security import generate_password_hash, check_password_hash

# logger = logging.getLogger("werkzeug")


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ac14134bafcd10c28a0e38d58dac3096'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = 'static/files/cheat_sheet.pdf'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        hash_salt = generate_password_hash(
            request.form.get('password'),
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User(
        name=request.form["name"],
        email=request.form.get("email"),
        password=hash_salt,
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
        else:
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=request.args.get('name'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # file = request.args.get('file')
    # if file:
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
