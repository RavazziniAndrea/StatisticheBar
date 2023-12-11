FROM python:3.8-slim

WORKDIR /

COPY common/ /WebApp/app

WORKDIR /WebApp/app

COPY /WebApp/app/requirementsWebApp.txt .

RUN pip install -r requirementsWebApp.txt

COPY /WebApp/app .

CMD ["python", "web_app.py"]