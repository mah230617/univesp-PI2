from dotenv import load_dotenv
from flask import Flask, session
from werkzeug.security import generate_password_hash
from database.database import db
from routes.login_routes import login_bp
from routes.usuario_routes import usuario_bp
from routes.cliente_routes import cliente_bp
from routes.home_routes import home_bp
from models.usuario import Usuario
from models.cliente import Cliente
from models.endereco import Endereco
from services.startup_service import criar_usuario_admin
from datetime import timedelta
from utils.formatters import formatar_cpf_cnpj, formatar_telefone, formatar_cep, formatar_data
import os

load_dotenv()

app = Flask(__name__)

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv('DEBUG', 'False').lower() == 'true'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=int(os.getenv("SESSION_TIMEOUT", 30)))

if not app.config["SQLALCHEMY_DATABASE_URI"]:
    raise ValueError("DATABASE_URL não configurada")

db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(cliente_bp)

with app.app_context():

    db.create_all()

    criar_usuario_admin()

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.url_map.strict_slashes = False

@app.context_processor
def inject_user():
    return {
        'usuario_logado': session.get('username'),
        'usuario_admin': session.get('administrador')
    }

@app.before_request
def renovar_sessao():
    session.permanent = True
    session.modified = True

app.jinja_env.globals.update(
    formatar_cpf_cnpj= formatar_cpf_cnpj,
    formatar_telefone= formatar_telefone,
    formatar_cep= formatar_cep,
    formatar_data= formatar_data
)

if __name__ == '__main__':
    app.run(debug=True)