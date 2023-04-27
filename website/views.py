from flask import Blueprint, render_template, request
from .model import Note
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/notes', methods=['POST', 'GET'])
def notes():
    if request.method == 'POST':
        note = request.form.get("note")
        if len(note) > 1:
            n = Note(text=note)
            db.session.add(n)
            db.session.commit()
            print("СОЗДАНА НОВАЯ ЗАПИСЬ")

    notes = db.session.query(Note).limit(10)

    return render_template("notes.html", notes=notes)
