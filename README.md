# Projeto Integrador II - Eixo de Computação (UNIVESP)
## Disciplina DRP01 - Turma 004

# Sistema com Acessibilidade de Cadastro de Clientes
### Estudo de Caso e Solução Aplicada: Visual Produções

---

## 🎓 Identificação Acadêmica

* **Instituição:** Universidade Virtual do Estado de São Paulo (UNIVESP)
* **Disciplina:** Projeto Integrador II (DRP01 - Turma 004)
* **Eixo:** Computação (Engenharia de Computação, Ciência de Dados, Tecnologia da Informação)
* **Tutor Responsável:** Nicole da Costa Cerqueira
* **Ano:** 2026

---

## 👥 Integrantes do Grupo

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

## 📖 Visão Geral e Contextualização do Problema

A empresa parceira **Visual Produções** operava com fluxos cadastrais fragmentados, baseados em rotinas manuais ou interfaces legadas desprovidas de padronização, validações automáticas e, principalmente, sem qualquer recurso de acessibilidade digital. Isso acarretava inconsistências em cadastros (documentos incorretos, duplicações de registros, erros de CEP) e restringia a operação autônoma por parte de pessoas com deficiência visual, baixa visão ou pessoas surdas.

Este projeto entrega uma solução web completa, robusta e inclusiva de **Gerenciamento de Clientes e Usuários (CRUD)**, garantindo:
1. **Integridade e Consistência de Dados:** Validação matemática estrita de CPF/CNPJ, controle de duplicidades, formatação de contatos e auto-completar de logradouro via CEP.
2. **Acessibilidade Universal:** Plena conformidade com as diretrizes internacionais da **WCAG 2.1 (Nível AA)** e do **e-MAG** (Modelo de Acessibilidade do Governo Eletrônico).
3. **Escalabilidade e Segurança:** Arquitetura em camadas (MVC com Services e Blueprints), proteção contra injeções, controle de acessos administrativos, senhas criptografadas e persistência relacional.

---

## 📋 Ementa do Projeto Integrador e Mapeamento no Código

A tabela a seguir demonstra a correspondência direta entre as competências da ementa acadêmica da UNIVESP e sua implementação técnica no repositório:

| Item da Ementa | Descrição da Implementação | Localização no Código-Fonte |
| :--- | :--- | :--- |
| **Resolução de problemas** | Regras de integridade para prevenção de duplicidade (CPF/CNPJ/e-mail), validação algorítmica de documentos, normalização de dados e tratamento seguro de erros. | `services/cliente_service.py`, `services/usuario_service.py` e `utils/formatters.py` |
| **Levantamento de requisitos** | Documentação detalhada dos fluxos funcionais, diagramas, casos de uso e especificações técnicas de acessibilidade. | Pasta `docs/` e `README.md` |
| **Desenvolvimento web com framework** | Aplicação Backend estruturada em **Python** com o framework **Flask**, arquitetada em módulos com *Blueprints* (`login`, `home`, `cliente`, `usuario`). | `app.py`, `routes/login_routes.py`, `routes/home_routes.py`, `routes/cliente_routes.py`, `routes/usuario_routes.py` |
| **HTML, CSS** | Telas dinâmicas desenvolvidas em **HTML5 Semântico** (Jinja2), estilizadas com **CSS3** modular, layout responsivo para desktop/mobile e **Bootstrap 5**. | `templates/layout/index.html`, `templates/acesso/`, `templates/cliente/`, `templates/usuario/` e `static/css/style.css` |
| **Linguagem de script** | Scripts client-side em **JavaScript (Vanilla)** para máscaras dinâmicas, validação de campos, consulta assíncrona de CEP, barra de acessibilidade e controle do DOM. | `static/js/acessibilidade.js`, `static/js/cep.js`, `static/js/masks.js`, `static/js/form-validation.js`, `static/js/loading.js` e `static/js/alterar-icone.js` |
| **Banco de Dados** | Modelagem relacional e persistência de dados gerenciada via ORM **SQLAlchemy** (compatível com SQLite para desenvolvimento local e PostgreSQL para produção). | `database/database.py` e modelos em `models/usuario.py`, `models/cliente.py`, `models/endereco.py` |
| **Controle de Versão** | Rastreabilidade do desenvolvimento, versionamento colaborativo com Git, branch workflow e commits semânticos no GitHub. | Histórico Git, repositório remoto e arquivo `.gitignore` |
| **Nuvem** | Parametrização para hospedagem PaaS na nuvem (**Render**), com configuração de inicialização e variáveis de ambiente desacopladas. | `Procfile`, `requirements.txt`, `.env.example` e `.env` |
| **API** | Integração com a **API ViaCEP** (`https://viacep.com.br/ws/`) para busca assíncrona de endereços e integração com a **API do VLibras** (`https://vlibras.gov.br/app`). | `static/js/cep.js` e `templates/layout/index.html` |
| **Acessibilidade** | Suporte integral à **WCAG 2.1 AA / e-MAG**: leitor de tela (NVDA/JAWS), atalhos de salto (`Skip Link`), atributos ARIA, modo alto contraste adaptativo e widget oficial **VLibras com avatar Hozana**. | `templates/layout/index.html`, `static/js/acessibilidade.js`, `static/css/style.css` |
| **Testes** | Suíte completa com dezenas de testes automatizados cobrindo autenticação, permissões de admin, validações cadastrais, acessibilidade e persistência. | Pasta `tests/` (`test_login.py`, `test_cadastro_*.py`, `test_acesso_*.py`, etc.) |
| **Análise de dados** | Estruturação e higienização dos dados para ordenação, filtragem por critérios, busca textual e exportação/relatórios cadastrais. | `services/cliente_service.py` e consultas SQLAlchemy |

---

## ♿ Recursos de Acessibilidade Implementados (WCAG 2.1 AA / e-MAG)

O sistema foi concebido sob os princípios do **Desenho Universal**, garantindo usabilidade sem barreiras:

1. **Tradução em Libras (VLibras):**
   - Inclusão do widget governamental oficial com a avatar 3D **Hozana**, permitindo a tradução de textos em português para a Língua Brasileira de Sinais em tempo real.
2. **Modo Alto Contraste:**
   - Alternância com um clique no botão flutuante ou cabeçalho.
   - Esquema visual com fundo preto puro (`#000000`), tipografia e contornos em amarelo vibrante (`#ffff00`), elementos interativos em branco e *placeholders* em cinza claro legível (`#cccccc`), garantindo contraste superior a 13:1 (muito acima do índice mínimo de 4.5:1 exigido pela WCAG).
3. **Redimensionamento Fluido de Fonte (A-, A, A+):**
   - Escalonamento progressivo (Normal, Grande e Extra Grande) aplicado na raiz do documento (`<html>` e `<body>`), ajustando proporcionalmente todos os textos, botões, campos de entrada e tabelas do sistema com retenção de preferência via `localStorage`.
4. **Navegação por Leitores de Tela (NVDA, JAWS, VoiceOver):**
   - **Skip Link:** Link de salto visível no foco inicial (`Ir para o conteúdo principal`) para pular menus repetitivos.
   - **Semântica ARIA:** Emprego consistente de `aria-label`, `aria-required`, `aria-current="page"`, `aria-live="polite"` e estados `aria-pressed`.
   - **Eliminação de ruídos:** Ícones meramente ilustrativos demarcados com `aria-hidden="true"`.
5. **Navegação Completa por Teclado:**
   - Todos os botões, links e campos possuem indicadores visuais claros de foco (`focus-visible` com anel contrastante), sem armadilhas de teclado (*keyboard traps*).

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem Principal:** Python 3.10+ (compatível com 3.13)
* **Backend Framework:** Flask 3.x
* **ORM e Banco de Dados:** SQLAlchemy / Flask-SQLAlchemy (SQLite / PostgreSQL)
* **Frontend:** HTML5 Semântico, CSS3 Flexbox/Grid, Bootstrap 5.3
* **Scripting Client-side:** JavaScript Vanilla moderno (Fetch API, DOM manipulation)
* **Bibliotecas e Componentes Externos:**
  - **VLibras Plugin:** Tradução automatizada para Língua Brasileira de Sinais
  - **ViaCEP API:** Webservice gratuito para consulta de CEPs
  - **Flatpickr:** Seletor de datas acessível com suporte a pt-BR
  - **Vanilla-Masker:** Máscaras de entrada sem dependência de jQuery
  - **Bootstrap Icons:** Conjunto de ícones vetoriais acessíveis
* **Gerenciamento de Ambiente:** Python `venv` e `python-dotenv`
* **Testes Automatizados:** Suíte de testes unitários e de integração em `tests/`
* **Hospedagem em Nuvem:** Render (plataforma PaaS)

---

## 📁 Estrutura do Projeto

```txt
univesp-PI2/
│
├── app.py                      # Arquivo principal da aplicação e registro de rotas
├── auth.py                     # Decorators de autenticação e proteção de sessão
├── requirements.txt            # Dependências e pacotes Python do projeto
├── Procfile                    # Comando de inicialização para deploy no Render
├── .env.example                # Exemplo de configuração de variáveis de ambiente
├── .env                        # Variáveis locais (não versionadas)
├── README.md                   # Documentação do repositório
├── readme2.mk                  # Documentação detalhada atualizada do projeto
│
├── database/                   # Camada de conexão e inicialização do banco
│   └── database.py
│
├── docs/                       # Documentação técnica, relatórios e planos de ação
│   ├── DRP01 - Plano de Ação ...
│   └── DRP01 - Relatório Final ...
│
├── models/                     # Modelos de dados relacionais (SQLAlchemy)
│   ├── usuario.py              # Entidade Usuário (autenticação e perfis)
│   ├── cliente.py              # Entidade Cliente (dados cadastrais)
│   └── endereco.py             # Entidade Endereço (vinculada ao cliente)
│
├── routes/                     # Controladores e rotas organizados em Blueprints
│   ├── login_routes.py         # Autenticação, login e logout
│   ├── home_routes.py          # Dashboard e tela inicial
│   ├── cliente_routes.py       # CRUD completo e pesquisa de clientes
│   └── usuario_routes.py       # Gestão administrativa de usuários
│
├── services/                   # Camada de lógica e regras de negócio
│   ├── cliente_service.py      # Validações e persistência de clientes
│   ├── usuario_service.py      # Regras de cadastro e hashing de usuários
│   ├── startup_service.py      # Inicialização do banco e criação do admin padrão
│   └── utils_service.py        # Utilitários de negócio
│
├── static/                     # Arquivos estáticos servidos pelo navegador
│   ├── css/
│   │   ├── bootstrap.min.css   # Framework CSS base
│   │   └── style.css           # Estilos customizados, alto contraste e acessibilidade
│   ├── js/
│   │   ├── acessibilidade.js   # Controle de contraste, zoom de fonte e persistência
│   │   ├── cep.js              # Integração assíncrona com API ViaCEP
│   │   ├── masks.js            # Máscaras de CPF, CNPJ, Telefone e CEP
│   │   ├── form-validation.js  # Validações dinâmicas de formulário
│   │   ├── loading.js          # Feedback visual acessível de carregamento
│   │   └── alterar-icone.js    # Controle do alternador de visibilidade de senha
│   └── img/
│       ├── logo.png            # Logotipo da Visual Produções
│       └── favicon.svg         # Ícone da aplicação
│
├── templates/                  # Templates HTML renderizados com Jinja2
│   ├── layout/
│   │   └── index.html          # Template base com barra de acessibilidade e VLibras
│   ├── acesso/
│   │   └── login.html          # Tela de login com suporte a alto contraste e fontes
│   ├── cliente/
│   │   ├── lista.html          # Listagem paginada e busca de clientes
│   │   ├── novo.html           # Formulário acessível de cadastro
│   │   └── editar.html         # Formulário acessível de alteração
│   ├── home/
│   │   └── index.html          # Dashboard principal
│   └── usuario/
│       └── lista.html          # Painel de controle de usuários do sistema
│
├── tests/                      # Bateria de testes automatizados
│   ├── test_login.py           # Testes de autenticação e bloqueios
│   ├── test_cadastro_cpf_*.py  # Testes de validação de CPF
│   ├── test_cadastro_cnpj_*.py # Testes de validação de CNPJ
│   ├── test_mascaras.py        # Testes de formatação e máscaras
│   ├── test_responsividade.py  # Testes de layout responsivo
│   └── ...                     # Mais de 50 casos de teste implementados
│
└── utils/                      # Formatações e validadores auxiliares
    └── formatters.py           # Algoritmos de validação de CPF/CNPJ e sanitização
```

---

## ⚙️ Pré-Requisitos de Instalação

Para executar a aplicação localmente, certifique-se de possuir instalado:
* **Python 3.10 ou superior** (recomendado Python 3.13)
* **Git** para clonagem do repositório
* **Navegador web moderno** (Chrome, Firefox, Edge)

---

## 🚀 Guia de Instalação e Execução Passo a Passo

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/mah230617/univesp-PI2.git
cd univesp-PI2
```

### 2️⃣ Criar e Ativar o Ambiente Virtual (`venv`)

* **No Windows (PowerShell / Prompt):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

* **No Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

*(O terminal indicará `(venv)` no início da linha de comando).*

### 3️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (ou copie a partir de `.env.example`):

```bash
cp .env.example .env
```

Conteúdo padrão do arquivo `.env`:
```env
SECRET_KEY=chave-secreta-de-desenvolvimento-visual-producoes
DATABASE_URL=sqlite:///database.db
SESSION_TIMEOUT=30
DEBUG=True

ADMIN_USERNAME=projeto.admin
ADMIN_PASSWORD=mudar@123
```

### 5️⃣ Executar a Aplicação

```bash
python app.py
```

O terminal exibirá a inicialização do servidor de desenvolvimento:
```txt
* Running on http://127.0.0.1:5000
```

Abra o navegador e acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔐 Credenciais Padrão de Primeiro Acesso

O sistema realiza a inicialização automática do banco de dados na primeira execução e cria a conta administrativa padrão:

* **Usuário:** `projeto.admin`
* **Senha:** `mudar@123`

> ⚠️ **Recomendação:** Em ambientes de produção, altere a senha imediatamente após o primeiro login através do painel de Usuários.

---

## 🧪 Executando os Testes Automatizados

Para executar toda a bateria de testes automatizados do sistema:

```bash
pytest
```
ou utilizando o runner padrão do Python:
```bash
python -m unittest discover tests
```

---

## ☁️ Deploy em Nuvem (Render)

A aplicação está configurada para deploy simplificado em plataformas PaaS como o **Render**:
1. Conectar o repositório GitHub ao Render como um **Web Service**.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `gunicorn app:app` (ou o comando definido no `Procfile`).
4. Configurar as variáveis de ambiente (`SECRET_KEY`, `DATABASE_URL`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`) na aba *Environment* do painel do Render.

---

> *Projeto acadêmico desenvolvido para a disciplina de Projeto Integrador II da Universidade Virtual do Estado de São Paulo (UNIVESP), sob orientação docente e com foco em acessibilidade digital e impacto comunitário real.*

