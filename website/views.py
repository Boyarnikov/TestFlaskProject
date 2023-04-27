from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<H1> THIS IS MY HOME PAGE<H1>"


@views.route('/notes')
def notes():
    return "<H1> THIS IS MY PAGE FOR MY NOTES<H1>"
