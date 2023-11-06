FROM python:3.11

COPY .env .env

RUN export $(cat .env | xargs)

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 3000

ENV NAME slackbot-service

CMD ["python", "main.py"]