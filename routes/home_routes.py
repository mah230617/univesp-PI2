from flask import Blueprint, render_template, redirect, session, url_for
from auth import login_required
import locale
from datetime import datetime

home_bp = Blueprint("home", __name__)

@home_bp.route("/home")
@login_required
def index_home():
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

    hoje = datetime.now().strftime("%d de %B de %Y")

    return render_template("home/index.html", hoje = hoje)



