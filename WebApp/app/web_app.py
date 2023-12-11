import redis as Redis
import os
from flask import Flask, render_template, request, Response
from flask_sse import sse
from threading import Thread
from time import sleep

from Valori.valori_grafico import ValoriGrafico
from Valori.redis_publisher import RedisPublisher
import common_reader
from Exceptions import config_exception


template_dir = os.path.abspath("web/templates")
static_dir   = os.path.abspath("web/static")
app = Flask(__name__, template_folder=template_dir, static_url_path='', static_folder=static_dir)

redis = None
# redis = Redis.Redis(host="172.17.0.2", port="6379")

valori = None
stop = False

#Questo è il metodo usato per passare i dati al frontend. Qui devo già avere tutti i dati parsati e pronti da servire 
#I dati saranno: [tipo_grafico, asse x, valori]
#E saranno codificati in una stringa, magari in json così js è veloce a tirarli fuori
def event_stream():
    print ("iaooooo", flush=True)


@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")


@app.route('/grafici', methods=["POST"])
def grafici ():
    print("Grafici", flush=True)
    grafico = request.form['grafico']
    tempo =   request.form['tempo']

    valori = ValoriGrafico(grafico, tempo)
    return "AjaxBackendFinito"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/statistiche')
def statistiche():
    return render_template("statistiche.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    print("Avvio WebApp")
    redis = Redis.Redis(host=common_reader.redis_address, port=common_reader.redis_port)
    app.run(host="0.0.0.0")