# FastAPI - API de Supermercado

API REST para gerenciamento de itens de supermercado, desenvolvida com FastAPI seguindo as melhores práticas de arquitetura modular.

## Características

- CRUD completo de itens
- Validação de dados com Pydantic
- Arquitetura modular (routers, services, models, database)
- Documentação automática com Swagger/ReDoc
- Armazenamento em memória

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

## Como Executar

Execute o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em: `http://127.0.0.1:8000`

## Endpoints Disponíveis

### GET /
Health check da API.

**Exemplo:**
```bash
curl http://127.0.0.1:8000/
```

### POST /items
Cria um novo item no supermercado.

**Body:**
```json
{
  "nome": "Arroz",
  "preco": 25.90,
  "quantidade": 100,
  "categoria": "Grãos"
}
```

**Exemplo:**
```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Arroz","preco":25.90,"quantidade":100,"categoria":"Grãos"}'
```

### GET /items
Retorna todos os itens ou um item específico.

**Parâmetros:**
- `item_id` (opcional): ID do item para buscar apenas um

**Exemplos:**
```bash
# Todos os itens
curl http://127.0.0.1:8000/items

# Item específico
curl http://127.0.0.1:8000/items?item_id=1
```

### PUT /items/{item_id}
Atualiza um item existente (atualização parcial).

**Body (todos os campos são opcionais):**
```json
{
  "nome": "Arroz Integral",
  "preco": 28.90
}
```

**Exemplo:**
```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"preco":28.90}'
```

### DELETE /items/{item_id}
Deleta um item do supermercado.

**Exemplo:**
```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

## Documentação Interativa

O FastAPI gera automaticamente documentação interativa:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Estrutura do Projeto

```
fastApiTest/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point da aplicação
│   ├── models/              # Schemas Pydantic (validação)
│   │   ├── __init__.py
│   │   └── item.py         # Item, ItemCreate, ItemUpdate
│   ├── routers/            # Endpoints HTTP
│   │   ├── __init__.py
│   │   └── items.py        # Rotas CRUD de itens
│   ├── services/           # Lógica de negócio
│   │   ├── __init__.py
│   │   └── item_service.py # Regras de negócio dos itens
│   └── database/           # Armazenamento
│       ├── __init__.py
│       └── db.py           # Database em memória
├── venv/                   # Ambiente virtual
├── requirements.txt        # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## Arquitetura

O projeto segue uma arquitetura em camadas:

- **Models**: Schemas Pydantic para validação de dados
- **Routers**: Endpoints HTTP (recebe requisições, retorna respostas)
- **Services**: Lógica de negócio (regras, validações complexas)
- **Database**: Camada de persistência (atualmente em memória)
