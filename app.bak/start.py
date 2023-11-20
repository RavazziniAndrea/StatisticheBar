import redis as Redis
import os
from flask import Flask, render_template, request, Response
from flask_sse import sse
from threading import Thread
from time import sleep

import DatabaseUtils.database_handler as database_handler
from Valori.valori_grafico import ValoriGrafico
from config_reader import ConfigReader

template_dir = os.path.abspath("web/templates")
static_dir   = os.path.abspath("web/static")
app = Flask(__name__, template_folder=template_dir,
            static_url_path='', 
            static_folder=static_dir)

redis = Redis.Redis(host="172.17.0.2", port="6379")
# redis = Redis.Redis(host="172.18.0.2", port="6379")

valori = None
stop = False
thread_grafico = Thread()
thread_database = Thread()

#Questo è il metodo usato per passare i dati al frontend. Qui devo già avere tutti i dati parsati e pronti da servire 
#I dati saranno: [tipo_grafico, asse x, valori]
#E saranno codificati in una stringa, magari in json così js è veloce a tirarli fuori
def event_stream():
    pubsub = redis.pubsub()
    pubsub.subscribe('totaldb')
    # pubsub.subscribe('datidb')
    try:
        for message in pubsub.listen():
            # print (message)
            # TODO gestire il primo messaggio che arriva, dato che è diverso dagli altri
            yield 'data: %s\n\n' % message['data']
    finally:
        print("Esco")
        global stop
        stop = True


@app.route('/stream')
def stream():
    # TODO Gestire il stop thread, da rimettere a True
    print("Avvio thread lettura database")
    global thread_database
    if(thread_database.is_alive()):
        database_handler.stop_query()
        thread_database.join()
        print("thread database stoppato")
    thread_database = Thread(target=get_dati)
    thread_database.start()
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
    tempo =   request.form['tempo']

    valori = ValoriGrafico(grafico, tempo)
    print("qui")

    print("Avvio thread lettura valori redis")
    global thread_grafico
    thread_grafico = Thread(target=valori.scrivi_grafico)
    thread_grafico.start()

    # valori.scrivi_grafico()

    print("dati salvati: "+grafico + " -- " +tempo)
    return "AjaxBackendFinito"


@app.route('/about')
def about():
    return render_template("about.html")


def get_dati():
    database_handler.get_dati_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)