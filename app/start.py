from flask import Flask, render_template, request, Response
from flask_sse import sse
from threading import Thread
from time import sleep
import redis as Redis
import os
from Valori.valori_grafico import ValoriGrafico
import DatabaseUtils.database_handler as database_handler
from config_reader import ConfigReader

template_dir = os.path.abspath("web/templates")
static_dir   = os.path.abspath("web/static")
app = Flask(__name__, template_folder=template_dir,
            static_url_path='', 
            static_folder=static_dir)

redis = Redis.Redis(host="172.17.0.2", port="6379")

valori = None
stop = False

def event_stream():
    pubsub = redis.pubsub()
    pubsub.subscribe('datidb')
    try:
        for message in pubsub.listen():
            print (message)
            # TODO gestire il primo messaggio che arriva, dato che è diverso dagli altri
            yield 'data: %s\n\n' % message['data']
    finally:
        print("Esco")
        global stop
        stop = True


@app.route('/stream')
def stream():
    # TODO Gestire il stop thread, da rimettere a True
    print("Avvio thread")
    thread = Thread(target=get_dati)
    thread.start()
    print("Thread avviato")
    return Response(event_stream(), mimetype="text/event-stream")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/statistiche')
def statistiche():
    return render_template("statistiche.html")


@app.route('/grafici', methods=["POST"])
def grafici ():
    grafico = request.form['grafico']
    tempo   = request.form['tempo']
    global valori
    valori = ValoriGrafico(grafico, tempo)

    valori.scrivi_grafico()

    print("dati salvati: "+grafico + " -- " +tempo)
    return "AjaxBackendFinito"


@app.route('/about')
def about():
    return render_template("about.html")


def get_dati():
    database_handler.get_dati_db()


if __name__ == "__main__":
    app.run(host="localhost", threaded=True)