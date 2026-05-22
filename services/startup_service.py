import os
from werkzeug.security import generate_password_hash
from models.usuario import Usuario
from database.database import db


def criar_usuario_admin():

    username = os.getenv("ADMIN_NAME")
    senha = os.getenv("ADMIN_PASSWORD")

    if not username or not senha:
        raise ValueError("Variáveis do admin não configuradas no arquivo .env")

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario:
        return

    admin = Usuario(
        username=username,
        senha=generate_password_hash(senha),
        administrador=True
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin criado com sucesso!")