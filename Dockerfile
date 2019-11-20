FROM python:alpine

WORKDIR /backlog-app

COPY application ./application

COPY Procfile run.py requirements.txt ./

EXPOSE 5000

RUN apk add --no-cache python postgresql-dev gcc musl-dev &&\
    pip install Flask &&\
    pip install flask-sqlalchemy &&\
    pip install flask-wtf &&\
    pip install flask-login &&\
    pip install psycopg2 &&\
    apk del python postgresql-dev gcc musl-dev &&\
    addgroup -S app &&\
    adduser -S -G app app &&\
    chown app -R .

USER app

CMD ["python", "run.py"]