from database.database import db

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    cep = db.Column(db.String(9))
    logradouro = db.Column(db.String(100))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(2))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(50))