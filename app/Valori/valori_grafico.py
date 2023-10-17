import redis as Redis
from Exceptions.dati_non_validi_exception import DatiNonValidiException


redis = Redis.Redis(host="172.17.0.2", port="6379")

class ValoriGrafico:

    def __init__(self, grafico, tempo):
        if not self.check_valid(grafico, tempo):
            raise DatiNonValidiException("Valori a null. Errore")
        self.grafico = grafico
        self.tempo = tempo

    def scrivi_grafico(self):
        pubsub = redis.pubsub()
        pubsub.subscribe("datidb")
        for mess in pubsub.listen():
            #TODO, impostare da qui i dati per il tipo di grafico selezionato, po inviarli
            yield 1

    def check_valid(self, grafico, tempo):
        return grafico != None and tempo != None 

    def get_grafico(self):
        return self.grafico
    
    def set_grafico(self, grafico):
        self.grafico = grafico

    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, tempo):
        self.tempo = tempo