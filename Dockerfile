FROM python:3.11.1-slim

# set work directory
WORKDIR /app
# COPY ./app /app
COPY ./app .

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN pip install fastapi; pip install uvicorn
RUN pip install -r config/requirements.txt
RUN apt update && apt -y install libpq-dev gcc && pip install psycopg2

RUN export FLASK_APP=start
#RUN cd app
CMD ["flask", "run"]
