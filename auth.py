from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if 'username' not in session:
            return redirect(url_for('login.login'))

        return func(*args, **kwargs)

    return wrapper

def admin_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        if not session.get('administrador'):

            flash('Acesso negado', 'danger')

            return redirect(url_for('home.index_home'))

        return f(*args, **kwargs)

    return wrapper