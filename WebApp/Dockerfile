FROM python:3.8-slim

WORKDIR /

COPY requirementsWebApp.txt .

RUN pip install -r requirementsWebApp.txt

COPY . .

WORKDIR /app

CMD ["python", "web_app.py"]