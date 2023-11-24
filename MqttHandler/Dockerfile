FROM python:3.8-slim

WORKDIR /

COPY requirementsMqtt.txt .

RUN pip install -r requirementsMqtt.txt

COPY . .

WORKDIR /app

CMD ["python", "mqttHandler.py"]