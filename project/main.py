from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    db.create_all()
    return render_template("index.html")

@main.route('/profile')
def profile():
    hidden_word="_____"
    db.create_all()
    return render_template("profile.html", hidden_word=hidden_word)
    # hidden_word = html; antras hidden_word = kintamasis; (realybeje imti is programos) = 12 eilute