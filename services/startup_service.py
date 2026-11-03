import os
from werkzeug.security import generate_password_hash
from models.usuario import Usuario
from database.database import db


def criar_usuario_admin():

    username = os.getenv("ADMIN_USERNAME") or os.getenv("ADMIN_NAME") or "admin"
    senha = os.getenv("ADMIN_PASSWORD") or "admin123"

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