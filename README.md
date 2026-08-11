# Projeto Integrador II - Eixo de Computação (UNIVESP) - Disciplina DRP01 - Turma 004

## NOME DO PROJETO

Este repositório contém o desenvolvimento do projeto acadêmico voltado à padronização e estruturação de dados de clientes, com foco em integridade, organização e escalabilidade de informações.

---

### 🎓 Instituição
**Universidade Virtual do Estado de São Paulo (UNIVESP)** **Disciplina:** Projeto Integrador II  
**Eixo:** Computação  

---

### 👥 Integrantes do Grupo

| Nome | RA | Polo | Curso |
| :--- | :--- | :--- | :--- |
| **Aline Lima da Silva** | 2233362 | Polo Itaquaquecetuba | Tecnologia da Informação |
| **André Schiavone Nanete** | 24210889 | Polo Diadema | Tecnologia da Informação |
| **Christofer Vagner Olivares** | 24203621 | Polo Cajamar | Engenharia da Computação |
| **Diego Lucas de Oliveira** | 2203023 | Polo Diadema | Tecnologia da Informação |
| **Emily Thomaz Lima** | 23217845 | Polo Jandira | Engenharia da Computação |
| **Larissa de Souza Aguiar** | 24206943 | Polo Embu das Artes | Ciência de Dados |
| **Luciano Carneiro da Silva** | 1702980 | Polo Carapicuiba | Engenharia da Computação |
| **Maíra Silva Edo** | 24203688 | Polo Diadema | Ciência de Dados |

---

### 🎯 Objetivo do Projeto
O projeto visa:
* **Padronização:** Garantir que os dados inseridos sigam regras de negócio estabelecidas.
* **Integridade:** Evitar duplicidade e inconsistências na base de dados.
* **Prática Acadêmica:** Aplicar os conhecimentos adquiridos ao longo dos semestres do eixo de computação.
* **Objetivo Acadêmico:** Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente incluir análises de dados.
* **Ementa:** Resolução de problemas; Levantamento de requisitos; Desenvolvimento web com framework; HTML, CSS; linguagem de script; Banco de Dados; Controle de Versão; Nuvem; API; Acessibilidade; Testes; Análise de dados;

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem de Programação:** Python 3
* **Framework Backend:** Flask
* **Banco de Dados:** SQLite / PostgreSQL
* **ORM:** SQLAlchemy
* **Frontend:** HTML5, CSS3, JavaScript e Bootstrap 5
* **Versionamento:** Git e GitHub
* **Gerenciamento de Dependências:** Pip (`requirements.txt`)
* **Variáveis de Ambiente:** Python Dotenv (`.env`)
* **Documentação:** Markdown
* **Hospedagem / Deploy:** Render

---

## 📁 Estrutura de Diretórios

```txt
Projeto_Integrador_I/
│── app.py
│── requirements.txt
│── Procfile
│── .env
│
├── auth/
│   └── Middleware de autenticação e autorização
│
├── database/
│   └── Configuração da conexão com banco de dados
│
├── docs/
│   └── Documentação técnica e relatórios do Projeto Integrador
│
├── models/
│   └── Modelos das entidades do sistema (Usuário, Cliente, Endereço)
│
├── routes/
│   └── Rotas e controladores da aplicação
│
├── services/
│   └── Regras de negócio e serviços da aplicação
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── Arquivos estáticos do sistema
│
├── templates/
│   └── Páginas HTML renderizadas pelo Flask (Jinja2)
│
└── utils/
    └── Funções auxiliares e formatações
```

---

## ⚙️ Pré-Requisitos

Antes de executar o projeto localmente, é necessário possuir instalado:

* ✔ **Python 3.13 ou superior**
* ✔ **Visual Studio Code**
* ✔ **Git**

---

## 💻 Instalação do Ambiente

### 1️⃣ Instalar o Visual Studio Code

Acesse o site oficial:

https://code.visualstudio.com/

Baixe e instale a versão para Windows.

Durante a instalação, recomenda-se marcar:

* ✔ Add to PATH
* ✔ Open with Code

---

### 2️⃣ Instalar o Python

Acesse:

https://www.python.org/downloads/

Baixe a versão mais recente do Python.

Durante a instalação, marque obrigatoriamente:

✔ **Add Python to PATH**

Após instalar, valide no terminal:

```bash
python --version
```

Exemplo esperado:

```bash
Python 3.13.x
```

---

### 3️⃣ Instalar o Git

Acesse:

https://git-scm.com/download/win

Após instalar, valide:

```bash
git --version
```

Exemplo:

```bash
git version 2.x.x
```

---

## 📥 Clonando o Projeto

Abra o terminal e execute:

```bash
git clone https://github.com/mah230617/univesp-PI2.git
```

Acesse a pasta do projeto:

```bash
cd univesp-PI2
```

---

## 🐍 Configurando Ambiente Virtual

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Se tudo estiver correto, aparecerá:

```txt
(venv)
```

no terminal.

---

## 📦 Instalando Dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

Este comando instalará automaticamente todas as dependências necessárias.

---

## ⚙️ Configuração do Arquivo `.env`

Criar um arquivo chamado:

```txt
.env
```

Na raiz do projeto.

Exemplo:

```env
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sqlite:///database.db
SESSION_TIMEOUT=30
DEBUG=True

ADMIN_USERNAME=projeto.admin
ADMIN_PASSWORD=mudar@123
```

---

## ▶️ Executando a Aplicação

No terminal do VS Code execute:

```bash
python app.py
```

Se tudo estiver correto, será exibido:

```txt
Running on http://127.0.0.1:5000
```

---

## 🌐 Acessando o Sistema

Abra o navegador e acesse:

```txt
http://127.0.0.1:5000
```

---

## 🔐 Login Inicial

**Usuário:**

```txt
projeto.admin
```

**Senha:**

```txt
mudar@123
```

O usuário administrador é criado automaticamente no primeiro acesso.

---
> *Este projeto faz parte da grade curricular da UNIVESP e possui fins estritamente educativos e de pesquisa.*
