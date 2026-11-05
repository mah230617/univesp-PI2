import os
from werkzeug.security import generate_password_hash
from models.usuario import Usuario
from database.database import db


def _garantir_admin(username, senha):
    if not username or not senha:
        return

    usuario = Usuario.query.filter_by(username=username).first()
    if usuario:
        usuario.administrador = True
        usuario.senha = generate_password_hash(senha)
        db.session.commit()
        print(f"Admin '{username}' atualizado com sucesso!")
        return

    admin = Usuario(
        username=username,
        senha=generate_password_hash(senha),
        administrador=True
    )
    db.session.add(admin)
    db.session.commit()
    print(f"Admin '{username}' criado com sucesso!")


def criar_usuario_admin():
    # Cria/atualiza o usuário MASTER se definido
    master_user = os.getenv("MASTER_USERNAME")
    master_pwd = os.getenv("MASTER_PASSWORD")
    if master_user and master_pwd:
        _garantir_admin(master_user, master_pwd)

    # Cria/atualiza o usuário ADMIN configurado
    admin_user = os.getenv("ADMIN_USERNAME") or os.getenv("ADMIN_NAME")
    admin_pwd = os.getenv("ADMIN_PASSWORD")

    # Se não houver nenhum especificado, mantém compatibilidade com default "master"
    if not admin_user and not master_user:
        admin_user = "master"

    if admin_user and admin_pwd and admin_user != master_user:
        _garantir_admin(admin_user, admin_pwd)
