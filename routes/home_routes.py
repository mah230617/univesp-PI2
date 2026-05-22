from flask import Blueprint, render_template
from auth import login_required
from datetime import datetime

home_bp = Blueprint("home", __name__)

def formatar_data_pt(data):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return f"{data.day} de {meses[data.month - 1]} de {data.year}"


@home_bp.route("/home")
@login_required
def index_home():
    hoje = formatar_data_pt(datetime.now())

    return render_template("home/index.html", hoje=hoje)