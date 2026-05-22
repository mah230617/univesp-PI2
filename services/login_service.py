from models.usuario import Usuario
from werkzeug.security import (check_password_hash)

def validar_login(username, senha):

    usuario = Usuario.query.filter_by(username=username, status=True).first()
    
    return usuario if usuario and check_password_hash(usuario.senha, senha) else None