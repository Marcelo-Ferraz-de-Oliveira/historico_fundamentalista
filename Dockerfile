FROM python:3.11-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Exponha a porta em que o Gunicorn irá rodar
EXPOSE 8000

# Comando para iniciar o servidor Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "historico_fundamentalista.wsgi:application"]
