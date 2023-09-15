# Use uma imagem base do Python
FROM python:3.8.10

# Defina um diretório de trabalho no contêiner
WORKDIR /app

# Copie o código do aplicativo para o contêiner
COPY . /app

# Instale as dependências do aplicativo (se houver um arquivo requirements.txt)
RUN pip install -r requirements.txt

# Exponha a porta em que o servidor web estará ouvindo (por exemplo, porta 80)
EXPOSE 8000
 
# Comando para iniciar o servidor web Python
CMD ["uvicorn", "main:app"]