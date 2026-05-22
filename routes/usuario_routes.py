from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from services.usuario_service import obter_lista_usuarios, criar_usuario, alterar_status_usuario, validar_existe_usuario, normalizar_username
from auth import login_required, admin_required

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuario")

@usuario_bp.route("/lista")
@login_required
@admin_required
def listar_usuarios():
    return render_template("usuario/lista.html", usuarios=obter_lista_usuarios())

@usuario_bp.route("/novo", methods=["POST"])
@login_required
@admin_required
def novo_usuario():

    username = request.form.get("username")
    username_normalizado = normalizar_username(username)
    
    if validar_existe_usuario(username_normalizado):
        flash(f"O usuário '{username_normalizado}' já está cadastrado no sistema.", "danger")
    else:
        senha = request.form.get("senha")

        criar_usuario(username_normalizado, senha)

        flash("Usuário criado com sucesso!", "success")

    return redirect(url_for("usuario.listar_usuarios"))

@usuario_bp.route('/alterarstatus/<int:id>')
@login_required
@admin_required
def alterar_status(id):

    status_alterado = alterar_status_usuario(id)

    if not status_alterado: flash('Usuário não pode ser alterado.')

    return redirect(url_for("usuario.listar_usuarios"))