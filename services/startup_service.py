import os
from werkzeug.security import generate_password_hash
from models.usuario import Usuario
from database.database import db


def criar_usuario_admin():

    username = os.getenv("ADMIN_USERNAME") or os.getenv("ADMIN_NAME") or "master"
    senha = os.getenv("ADMIN_PASSWORD")

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario:
        usuario.administrador = True
        db.session.commit()
        return

    if not senha:
        return

    admin = Usuario(
        username=username,
        senha=generate_password_hash(senha),
        administrador=True
    )

    db.session.add(admin)
    db.session.commit()

    print(f"Admin '{username}' criado com sucesso!")