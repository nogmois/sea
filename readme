# Seazone Project

Este é um projeto Django que oferece uma API para gerenciar propriedades, anúncios e reservas. O sistema permite criar, visualizar, atualizar e deletar registros desses itens.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.10
- Django 3.2

### Instalação e Configuração

Clone o repositório e configure o ambiente de desenvolvimento:

```bash
# Clone o repositório
git clone https://github.com/nogmois/sea.git

# Entre no diretório do projeto
cd seazone_project

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Unix ou MacOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate
```
## Configuração Inicial

### Criando um Superusuário

Para administrar o site pelo Django Admin, você precisará criar um superusuário. Execute o seguinte comando:

```bash
python manage.py createsuperuser
```

## Executando o Projeto

Inicie o servidor Django com o seguinte comando:

```bash
python manage.py runserver

```
## Endpoints da API

### Propriedades (Properties)

- **Listar Propriedades (GET /properties/):** Retorna uma lista de todas as propriedades.
- **Criar Propriedade (POST /properties/):** Adiciona uma nova propriedade.

### Anúncios (Advertisements)

- **Listar Anúncios (GET /advertisements/):** Retorna uma lista de todos os anúncios.
- **Criar Anúncio (POST /advertisements/):** Adiciona um novo anúncio.

### Reservas (Reservations)

- **Listar Reservas (GET /reservations/):** Retorna uma lista de todas as reservas.
- **Criar Reserva (POST /reservations/):** Adiciona uma nova reserva.

### Autenticação

- **Obter Token (POST /api/token/):** Retorna um token de acesso para autenticação.
## Acesso a Áreas Protegidas

Para acessar áreas protegidas da API, como as operações POST, PUT e DELETE, você precisará obter um token de acesso usando suas credenciais de superusuário.

### Obtendo um Token de Acesso

1. Envie uma solicitação POST para `/api/token/` com seu nome de usuário e senha para obter o token. Isso pode ser feito usando o cURL ou outra ferramenta similar.

2. Inclua o token de acesso no cabeçalho `Authorization` das suas solicitações para acessar as áreas protegidas da API.

### Exemplo de Solicitação para Obter o Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=seu_usuario&password=sua_senha"
