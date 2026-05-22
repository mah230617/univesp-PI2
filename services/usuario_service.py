from models.usuario import Usuario
from database.database import db
from werkzeug.security import generate_password_hash
import re
import unicodedata

def obter_lista_usuarios():
    return Usuario.query.filter(Usuario.username != 'admin').all()

def criar_usuario(username, senha):
    usuario = Usuario(
        username = username,
        senha = generate_password_hash(senha),
        administrador = False,
        status = True
    )
    db.session.add(usuario)
    db.session.commit()

def alterar_status_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    if usuario.username == 'admin': return False

    usuario.status = not usuario.status

    db.session.commit()

    return True

def validar_existe_usuario(username):
    return Usuario.query.filter_by(username=username).first() is not None

def normalizar_username(username):
    if not username:
        return None

    # remove acentos
    username = unicodedata.normalize("NFKD", username)
    username = "".join(c for c in username if not unicodedata.combining(c))

    # remove espaços e substitui por ponto
    username = username.strip().lower()
    username = re.sub(r"\s+", ".", username)

    # remove caracteres inválidos
    username = re.sub(r"[^a-z0-9._]", "", username)

    return username