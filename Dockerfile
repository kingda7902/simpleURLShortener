FROM python:3.7-slim

WORKDIR /code
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./app

ENV FLASK_APP app/app.py

CMD python3 -m flask run
