from database.database import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cpfcnpj = db.Column(db.String(14), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    enderecos = db.relationship("Endereco", backref="cliente", lazy=True)