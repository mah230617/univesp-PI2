from models.cliente import Cliente
from models.endereco import Endereco
from database.database import db
from services.utils_service import somente_numeros, converter_data

def criar_editar_cliente(cliente_id, dados_cliente):

    cpfcnpj = somente_numeros(dados_cliente['cpfcnpj'])
    telefone = somente_numeros(dados_cliente['telefone'])
    data_nascimento = converter_data(dados_cliente['data_nascimento'])

    if cliente_id:
        cliente = Cliente.query.get_or_404(cliente_id)

        cliente.nome = dados_cliente['nome']
        cliente.email = dados_cliente['email']
        cliente.cpfcnpj = cpfcnpj
        cliente.data_nascimento = data_nascimento
        cliente.telefone = telefone
    else:
        cliente = Cliente(
            nome = dados_cliente['nome'],
            email = dados_cliente['email'],
            cpfcnpj = cpfcnpj,
            data_nascimento = data_nascimento,
            telefone = telefone
        )

        db.session.add(cliente)

    db.session.commit()

    criar_editar_endereco(cliente.id, dados_cliente)

    return cliente

def criar_editar_endereco(cliente_id, dados_cliente):

    endereco = Endereco.query.filter_by(cliente_id=cliente_id).first()

    cep = somente_numeros(dados_cliente["cep"])

    if endereco:
        endereco.cep = cep
        endereco.logradouro = dados_cliente["logradouro"]
        endereco.bairro = dados_cliente["bairro"]
        endereco.cidade = dados_cliente["cidade"]
        endereco.estado = dados_cliente["estado"]
        endereco.numero = dados_cliente["numero"]
        endereco.complemento = dados_cliente["complemento"]
    else:
        endereco = Endereco(
            cliente_id=cliente_id,
            cep=cep,
            logradouro=dados_cliente["logradouro"],
            bairro=dados_cliente["bairro"],
            cidade=dados_cliente["cidade"],
            estado = dados_cliente["estado"],
            numero=dados_cliente["numero"],
            complemento=dados_cliente["complemento"]
        )

        db.session.add(endereco)

    db.session.commit()

def obter_lista_clientes(dadosBusca):

    query = Cliente.query

    if dadosBusca:
        nome = dadosBusca.get("nome")
        cpfcnpj = somente_numeros(dadosBusca.get("cpfcnpj"))

        if nome:
            query = query.filter(Cliente.nome.ilike(f"%{nome}%"))

        if cpfcnpj:
            query = query.filter(Cliente.cpfcnpj.ilike(f"%{cpfcnpj}%"))

    return query.all()

def obter_dados_cliente(id):
    return Cliente.query.get_or_404(id)

def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)

    endereco = Endereco.query.filter_by(cliente_id=cliente.id).first()

    if endereco:
        db.session.delete(endereco)

    db.session.delete(cliente)
    db.session.commit()

def validar_existe_cliente(cpfcnpj, cliente_id=None):

    query = Cliente.query.filter(Cliente.cpfcnpj == somente_numeros(cpfcnpj))

    if cliente_id:
        query = query.filter(Cliente.id != cliente_id)

    return query.first() is not None