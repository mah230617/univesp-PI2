from flask import (Blueprint, render_template, request, redirect, session, url_for)
from datetime import datetime, timezone
from database.database import db
from models.audit import AccessSession, SystemLog
from services.login_service import validar_login

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():

    if "username" in session:
        return redirect(url_for("home.index_home"))

    if request.method == "POST":

        username = request.form.get("username")
        senha = request.form.get("senha")
        ip = request.headers.get("X-Forwarded-For", request.remote_addr or "").split(",")[0].strip()

        usuario = validar_login(username, senha)

        if usuario:
            session.permanent = True
            session["username"] = usuario.username
            session["usuario_id"] = usuario.id
            session["administrador"] = usuario.administrador

            try:
                now = datetime.now(timezone.utc)
                acc = AccessSession(username=usuario.username, ip_address=ip, login_at=now, last_seen=now)
                db.session.add(acc)
                db.session.add(SystemLog(username=usuario.username, event_type="LOGIN", details="Login realizado com sucesso", ip_address=ip, created_at=now))
                db.session.commit()
                session["access_session_id"] = acc.id
            except Exception:
                db.session.rollback()

            return redirect(url_for("home.index_home"))

        try:
            db.session.add(SystemLog(username=username or "desconhecido", event_type="LOGIN_FALHA", details="Tentativa de login com credenciais inválidas", ip_address=ip))
            db.session.commit()
        except Exception:
            db.session.rollback()

        return render_template("acesso/login.html", erro="Usuário ou senha inválidos", username=username)

    return render_template("acesso/login.html")

@login_bp.route("/logout")
def logout():
    sid = session.get("access_session_id")
    uname = session.get("username")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "").split(",")[0].strip()
    if sid or uname:
        try:
            now = datetime.now(timezone.utc)
            if sid:
                acc = db.session.get(AccessSession, sid)
                if acc:
                    acc.logout_at = now
                    acc.last_seen = now
            if uname:
                db.session.add(SystemLog(username=uname, event_type="LOGOUT", details="Usuário encerrou a sessão", ip_address=ip, created_at=now))
            db.session.commit()
        except Exception:
            db.session.rollback()

    session.clear()

    return redirect(url_for("login.login"))