from flask import Blueprint, render_template, request, redirect, url_for
from .model import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        u = User.query.filter_by(login=login).first()
        if u:
            if check_password_hash(u.password, password):
                login_user(u)
                return redirect(url_for('views.private_notes'))
            else:
                error = "Введён неправленый пароль"

        else:
            error = "Пользователь с такми логином не существует"

    return render_template("login.html", error=error, user=current_user)


@auth.route('/register', methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        if User.query.filter_by(login=login).first():
            error = "Пользователь с такми логином уже существует"

        else:
            u = User(login=login, password=generate_password_hash(password, 'sha256'))

            db.session.add(u)
            db.session.commit()

            login_user(u, remember=True)
            return redirect(url_for('views.private_notes'))

    return render_template("register.html", error=error, user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
