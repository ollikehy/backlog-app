FROM python:latest

WORKDIR /backlog-app

COPY . .

EXPOSE 5000

RUN apt-get update && apt-get -y install curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN pip install Flask
RUN pip install flask-sqlalchemy
RUN pip install flask-wtf
RUN pip install flask-login
RUN pip install psycopg2

CMD ["python", "run.py"]