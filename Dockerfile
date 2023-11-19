FROM python:3.8-slim

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

WORKDIR /app

CMD ["python", "start.py"]
