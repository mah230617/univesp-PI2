from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.cliente_service import criar_editar_cliente, obter_lista_clientes, obter_dados_cliente, excluir_cliente, validar_existe_cliente
from auth import login_required, admin_required
from services.utils_service import LISTAR_ESTADOS

cliente_bp = Blueprint("cliente", __name__, url_prefix="/cliente")

@cliente_bp.route("/lista", methods=["GET", "POST"])
@login_required
def listar_clientes():

    filtros = request.form if request.method == "POST" else {}

    clientes = obter_lista_clientes(filtros)

    return render_template("cliente/lista.html", clientes=clientes, nome=filtros.get("nome", ""), cpfcnpj=filtros.get("cpfcnpj", ""))

@cliente_bp.route('/novo')
@login_required
def novo_cliente():
    return render_template('cliente/novo.html', form={}, estados=LISTAR_ESTADOS)

@cliente_bp.route("/novo", methods=["POST"])
@login_required
def adicionar_cliente():
    
    cpfcnpj = request.form.get("cpfcnpj")

    if validar_existe_cliente(cpfcnpj):
        flash(f"O CPF/CNPJ {cpfcnpj} já está cadastrado no sistema.", "danger")

        return render_template('cliente/novo.html', form=request.form, estados=LISTAR_ESTADOS)
    else:
        criar_editar_cliente(None, request.form)

        flash("Cliente criado com sucesso!", "success")

    return redirect(url_for('cliente.listar_clientes'))

@cliente_bp.route('/editar/<int:id>')
@login_required
def editar_cliente(id):
    return render_template('cliente/editar.html', cliente=obter_dados_cliente(id), estados=LISTAR_ESTADOS)

@cliente_bp.route('/editar/<int:id>', methods=['POST'])
@login_required
def atualizar_cliente(id):

    cpfcnpj = request.form.get("cpfcnpj")

    if validar_existe_cliente(cpfcnpj, id):
        flash(f"O CPF/CNPJ {cpfcnpj} já está cadastrado no sistema.", "danger")
    else:
        criar_editar_cliente(id, request.form)

        flash("Cliente alterado com sucesso!", "success")

    return redirect(url_for('cliente.editar_cliente', id=id))

@cliente_bp.route('/delete/<int:id>')
@login_required
@admin_required
def deletar_cliente(id):

    excluir_cliente(id)

    return redirect(url_for('cliente.listar_clientes'))