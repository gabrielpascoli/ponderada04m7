
# Use a imagem base do Python
FROM python:3.8-slim

# Configuração de diretório de trabalho
WORKDIR /app

# Copie o código Flask para o contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta
EXPOSE 80

# Comando para executar o aplicativo Flask
CMD ["python", "app.py"]
