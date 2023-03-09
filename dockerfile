FROM python:3.10-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY service1.py /app
COPY service2.py /app
COPY service3.py /app
COPY sql_queries.py /app
COPY transaction.py /app
COPY for_container.py /app
COPY object.py /app

CMD ["python", "/app/for_container.py"]