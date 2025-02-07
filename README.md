# RAG_with_LanGraph
Um sistema Rag usando langchain, langgraph, pgvector e chainlit

## Comandos

### Instalar a versão do Pyhon do projeto
```bash
pyenv update
pyenv install --list | grep '3.12.1'
pyenv install 3.12.1
pyenv global 3.12.1
python --version
python3 --version
pyenv versions

```
### Virtual environment

#### Criar e Ativar

```bash
python -m venv .venv

source .venv/bin/activate
# ou
. .venv/Scripts/Activate

pip install -r requirements.txt
```

#### Desativar

```bash
deactivate
```
### Docker
### Subi o Banco de Dados
```bash
docker-compose up --build
```
