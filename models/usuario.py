from database.database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    administrador = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=True)