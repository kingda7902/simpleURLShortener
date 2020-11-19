FROM python:3.7-slim

WORKDIR /code
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./app

CMD gunicorn --reload --bind 0.0.0.0:8000 app.app:app
