# Resumo

## Tecnologias utilizadas

- Docker
- Flask
- Postgresql

## Tarefas

- Criar tabela creator
- Criar função de armazenar foto com boto3

### Ao atualizar tabela(models/albuns.py)

- Mudar
- resources/album.py
- schemas.py

### Comandos

- docker build -t nome_da_imagem .
- docker run -ip 5000:5000 nome_da_imagem

#### Comando com o código do container vinculado ao local

- docker run -ip 5000:5000 -w /app -v "$(pwd):/app" nome_da_imagem sh -c "flask run --host 0.0.0.0"
