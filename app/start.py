import redis as Redis
import os
from flask import Flask, render_template, request, Response
from flask_sse import sse
from threading import Thread
from time import sleep

import DatabaseUtils.database_handler as database_handler
from Valori.valori_grafico import ValoriGrafico
from Valori.redis_publisher import RedisPublisher
from config_reader import ConfigReader

template_dir = os.path.abspath("web/templates")
static_dir   = os.path.abspath("web/static")
app = Flask(__name__, template_folder=template_dir, static_url_path='', static_folder=static_dir)

redis = Redis.Redis(host="172.17.0.2", port="6379")
# redis = Redis.Redis(host="172.18.0.2", port="6379")

valori = None
stop = False

#Questo è il metodo usato per passare i dati al frontend. Qui devo già avere tutti i dati parsati e pronti da servire 
#I dati saranno: [tipo_grafico, asse x, valori]
#E saranno codificati in una stringa, magari in json così js è veloce a tirarli fuori
def event_stream():
    return "ciaooooo"


@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")

def start_thread_leggi_dati():
    thread_leggi_dati = Thread(target=RedisPublisher.leggi_e_pubblica)
    thread_leggi_dati.start()
    print("Thread lettura dati avviato")

def start_thread_get_dati():
    thread_get_dati = Thread(target=database_handler.get_dati_db)
    thread_get_dati.start()
    print("Thread dati db avviato")


@app.route('/grafici', methods=["POST"])
def grafici ():
    grafico = request.form['grafico']
    tempo =   request.form['tempo']

    valori = ValoriGrafico(grafico, tempo)
    return "AjaxBackendFinito"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/statistiche')
def statistiche():
    start_thread_get_dati()
    start_thread_leggi_dati()
    return render_template("statistiche.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)