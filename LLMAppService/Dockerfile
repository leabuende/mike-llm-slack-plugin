FROM python:3.11

COPY .env .env

RUN export $(cat .env | xargs)

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENV NAME llm-service


CMD ["python", "main.py"]