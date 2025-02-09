# RAG with LangGraph

Um sistema RAG (Retrieval-Augmented Generation) avançado usando LangChain, LangGraph, PGVector e Chainlit. O sistema permite processamento eficiente de documentos com embeddings persistentes e uma interface de chat interativa.

## 🚀 Tecnologias Utilizadas

- **Python**: 3.12.1
- **LangChain**: Framework para desenvolvimento de aplicações com LLMs
- **LangGraph**: Biblioteca para criação de fluxos complexos com LLMs
- **PGVector**: Extensão do PostgreSQL para busca de similaridade com vetores
- **Chainlit**: Interface de chat moderna para LLMs
- **OpenAI**: Provedor de LLM para processamento de linguagem natural
- **Docker & Docker Compose**: Containerização e orquestração de serviços

## 🛠️ Pré-requisitos

- Python 3.12.1
- Docker e Docker Compose
- Git

## 📁 Estrutura do Projeto

```
.
├── documents/                    # Documentos de entrada
├── notebooks/                    # modelo de rag inicial
├── src/
│   ├── agent/                   # Componentes do agente RAG
│   │   ├── nodes.py            # Implementação dos nós do grafo
│   │   ├── state.py            # Gerenciamento de estado
│   │   └── graph.py            # Definição do grafo
│   ├── agents/                  # Implementação dos agentes
│   │   └── retriever.py        # Configuração do retriever e retriever_tool
│   ├── data/                    # Processamento de dados
│   │   └── process_documents.py # Lógica de processamento de documentos
│   ├── database/               # Configuração do banco de dados
│   │   └── base.py            # Conexão com o banco de dados
│   ├── documents/              # Documentos para embeddings
│   │   └── ...                # Arquivos de documentos
│   ├── models/                 # Modelos de IA
│   │   ├── llm.py            # Configuração do modelo de chat
│   │   └── embeddings.py     # Configuração do modelo de embeddings
│   ├── service/               # Serviços da aplicação
│   │   ├── app.py            # Aplicação Chainlit
│   │   └── embeddings.py     # Serviço de embeddings
│   ├── utils/                 # Utilitários
│   │   
│   └── settings.py           # Configuração de variáveis de ambiente
├── .env                       # Variáveis de ambiente
├── .env.example              # Exemplo de variáveis de ambiente
├── docker-compose.yml        # Configuração do Docker Compose
├── chainlit.Dockerfile       # Dockerfile da aplicação Chainlit
├── embeddings.Dockerfile     # Dockerfile do serviço de embeddings
├── requirements.txt          # Dependências do projeto
└── README.md                # Documentação do projeto
```

### 📌 Descrição dos Componentes

#### Agent (Grafo RAG)
- `nodes.py`: Implementa os nós específicos do grafo RAG
- `state.py`: Gerencia o estado da conversação e contexto
- `graph.py`: Define a estrutura e fluxo do grafo de conversação

#### Agents (Retrievers)
- `retriever.py`: Implementa a lógica de recuperação de documentos e ferramentas de retrieval

#### Data
- `process_documents.py`: Lógica para processamento e preparação de documentos

#### Database
- `base.py`: Configuração e gerenciamento de conexões com o banco de dados

#### Models
- `llm.py`: Configuração e integração do modelo de chat
- `embeddings.py`: Configuração do modelo de embeddings

#### Service
- `app.py`: Interface Chainlit e ponto de entrada da aplicação
- `embeddings.py`: Processamento e armazenamento de embeddings

#### Utils
- `document_loader.py`: Funções para carregamento e processamento de documentos
- `vector_store.py`: Configuração e interação com PGVector

#### Configuração
- `settings.py`: Gerenciamento centralizado de variáveis de ambiente e configurações

## ⚙️ Configuração do Ambiente

### Preparação do Python
```bash
# Atualizar pyenv
pyenv update

# Instalar Python 3.12.1
pyenv install 3.12.1

# Definir como versão global
pyenv global 3.12.1

# Verificar instalação
python --version  # Deve mostrar 3.12.1
```

### Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
## Linux/MacOS
source .venv/bin/activate
## Windows
.\.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Desativar (quando necessário)
deactivate
```

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
# Banco de Dados
datasource_username=seu_usuario
datasource_password=sua_senha
datasource_name=nome_banco
datasource_port=5432

# APIs e Secrets
open_ai_api_key=sua_chave_groq
CHAINLIT_AUTH_SECRET=seu_segredo_chainlit
```

## 🚀 Executando o Projeto

### Usando Docker Compose (Todos os Serviços)
```bash
# Construir e iniciar todos os serviços
docker-compose up --build

# Para parar
docker-compose down
```

### Executando Serviços Separadamente

#### 1. Banco de Dados (PGVector)
```bash
# Iniciar apenas o banco
docker-compose up db -d

# Ou usando Docker diretamente
docker run -d \
  --name pgvector-container \
  -e POSTGRES_USER=seu_usuario \
  -e POSTGRES_PASSWORD=sua_senha \
  -e POSTGRES_DB=nome_banco \
  -p 5432:5432 \
  pgvector/pgvector:16
```

#### 2. Serviço de Embeddings
```bash
# Com Docker
docker-compose up embeddings

# Sem Docker (local)
python src/service/embeddings.py
```

#### 3. Aplicação Chainlit
```bash
# Com Docker
docker-compose up app

# Sem Docker (local)
chainlit run src/service/app.py --port 3500
```

## 📦 Versões dos Serviços no Docker Compose

```yaml
services:
  db:
    image: pgvector/pgvector:16
  
  embeddings:
    build:
      context: .
      dockerfile: embeddings.Dockerfile
    # Base image: python:3.12.1-slim
  
  app:
    build:
      context: .
      dockerfile: chainlit.Dockerfile
    # Base image: python:3.12.1-slim
```

## 🌐 Acessando os Serviços

- **Interface Chainlit**: http://localhost:3500
- **Banco PGVector**: localhost:5432

## 📝 Notas Adicionais

- O serviço de embeddings precisa ser executado antes da aplicação Chainlit
- Certifique-se de que todas as variáveis de ambiente estejam configuradas
- Para desenvolvimento, é recomendado executar os serviços separadamente
- Os logs de cada serviço podem ser visualizados com `docker-compose logs [service_name]`

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request