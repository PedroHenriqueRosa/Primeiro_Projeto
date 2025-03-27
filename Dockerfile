# Imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências (requirements.txt) para dentro do container
COPY app/requirements.txt /app/


# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o Django automaticamente
RUN pip install django

# Criação do projeto Django
RUN django-admin startproject meu_django_app .

# Expor a porta 8000 para acesso ao servidor
EXPOSE 8000

# Comando para rodar o servidor do Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
