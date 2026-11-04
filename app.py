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
from models.audit import AccessSession, SystemLog
from services.startup_service import criar_usuario_admin
from datetime import datetime, timedelta, timezone
from utils.formatters import formatar_cpf_cnpj, formatar_telefone, formatar_cep, formatar_data
import os

load_dotenv()

app = Flask(__name__)

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "univesp-default-secret-key-123")
app.config["DEBUG"] = os.getenv('DEBUG', 'False').lower() == 'true'

db_url = os.getenv("DATABASE_URL", "sqlite:///database.db")
if "@@" in db_url:
    db_url = db_url.replace("@@", "%40@")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=int(os.getenv("SESSION_TIMEOUT", 30)))

db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(cliente_bp)

with app.app_context():
    try:
        db.create_all()
        criar_usuario_admin()
    except Exception as e:
        print(f"[UNIVESP-PI2 AVISO BANCO] {e}", flush=True)

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
    sid = session.get("access_session_id")
    uname = session.get("username")
    if uname:
        try:
            now = datetime.now(timezone.utc)
            if sid:
                acc = db.session.get(AccessSession, sid)
                if acc and acc.logout_at is None:
                    acc.last_seen = now
                    db.session.commit()
            else:
                from flask import request
                ip = request.headers.get("X-Forwarded-For", request.remote_addr or "").split(",")[0].strip()
                acc = AccessSession(username=uname, ip_address=ip, login_at=now, last_seen=now)
                db.session.add(acc)
                db.session.commit()
                session["access_session_id"] = acc.id
        except Exception:
            db.session.rollback()

app.jinja_env.globals.update(
    formatar_cpf_cnpj= formatar_cpf_cnpj,
    formatar_telefone= formatar_telefone,
    formatar_cep= formatar_cep,
    formatar_data= formatar_data
)

if __name__ == '__main__':
    app.run(debug=True)