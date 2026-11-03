"""
Script para resetar ou definir a senha do administrador master no Univesp-PI2.
Pode ser executado localmente ou dentro do container Docker no Easypanel.

Uso:
  python scratch/reset_master_password.py [NOVA_SENHA] [NOME_USUARIO]

Exemplos:
  python scratch/reset_master_password.py
  python scratch/reset_master_password.py MinhaNovaSenha123
  python scratch/reset_master_password.py MinhaNovaSenha123 admin
"""

import os
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Carrega variáveis de ambiente (.env se existir)
from dotenv import load_dotenv
load_dotenv(PROJECT_ROOT / ".env")

# Garante tratamento caso DATABASE_URL tenha @ ou postgres://
db_url = os.getenv("DATABASE_URL", "sqlite:///database.db")
if "@@" in db_url:
    os.environ["DATABASE_URL"] = db_url.replace("@@", "%40@")

from app import app
from database.database import db
from models.usuario import Usuario
from werkzeug.security import generate_password_hash


def reset_password(new_password: str, username: str = None):
    with app.app_context():
        # Busca usuário administrador
        if username:
            user = Usuario.query.filter_by(username=username).first()
        else:
            # Procura primeiro admin ou usuário com id=1
            user = Usuario.query.filter_by(administrador=True).first()
            if not user:
                user = Usuario.query.first()

        if not user:
            print(f"[!] Nenhum usuário existente encontrado. Criando novo administrador...")
            target_user = username or os.getenv("ADMIN_USERNAME", "admin")
            novo_admin = Usuario(
                username=target_user,
                senha=generate_password_hash(new_password),
                administrador=True
            )
            db.session.add(novo_admin)
            db.session.commit()
            print(f"[SUCESSO] Administrador '{target_user}' criado com sucesso!")
            print(f"[INFO] Usuário: {target_user} | Nova senha definida.")
            return

        user.senha = generate_password_hash(new_password)
        user.administrador = True
        db.session.commit()
        print(f"[SUCESSO] Senha do master/administrador '{user.username}' resetada com sucesso!")
        print(f"[INFO] Usuário: {user.username} (ID: {user.id}) | Nova senha definida.")


if __name__ == "__main__":
    pwd = sys.argv[1] if len(sys.argv) > 1 else None
    usr = sys.argv[2] if len(sys.argv) > 2 else None

    if not pwd:
        try:
            import getpass
            pwd = getpass.getpass("Digite a nova senha para o administrador master: ")
        except Exception:
            pwd = input("Digite a nova senha para o administrador master: ")

    pwd = pwd.strip()
    if not pwd:
        print("[ERRO] A senha não pode ser vazia.")
        sys.exit(1)

    reset_password(pwd, usr)
