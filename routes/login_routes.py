from flask import (Blueprint, render_template, request, redirect, session, url_for)
from services.login_service import validar_login

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():

    if "username" in session:
        return redirect(url_for("home.index_home"))

    if request.method == "POST":

        username = request.form.get("username")
        senha = request.form.get("senha")

        usuario = validar_login(username, senha)

        if usuario:
            session.permanent = True
            session["username"] = usuario.username
            session["usuario_id"] = usuario.id
            session["administrador"] = usuario.administrador

            return redirect(url_for("home.index_home"))

        return render_template("acesso/login.html", erro="Usuário ou senha inválidos", username=username)

    return render_template("acesso/login.html")

@login_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login.login"))