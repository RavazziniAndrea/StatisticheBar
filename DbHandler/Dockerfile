FROM python:3.8-slim

WORKDIR /

COPY common/ /DbHandler/app

WORKDIR /DbHandler/app

COPY /DbHandler/app/requirementsDb.txt .

RUN pip install -r requirementsDb.txt

COPY /DbHandler/app .

RUN "ls"

CMD ["python", "app.py"]