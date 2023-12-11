import redis as Redis

import common_reader
from Exceptions.dati_non_validi_exception import DatiNonValidiException


redis = Redis.Redis(host=common_reader.redis_address, port=common_reader.redis_port)

class ValoriGrafico:

    def __init__(self, grafico, tempo):
        if not self.check_valid(grafico, tempo):
            raise DatiNonValidiException("Valori a null. Errore")
        self.grafico = grafico
        self.tempo = tempo
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe("datidb")
        print("FINITO", flush=True)


    def scrivi_grafico(self):
        print("dentro")
        num=0
        for mess in self.pubsub.listen():
            
            
        #     #TODO in questo punto ottengo tutti i dati dal db. 
        #     # 1. Parsare i dati in record (dato_db.py)
        #     # 2. Creare le aggregazioni in base al grafico richiesto
        #     # 3. Pubblicare i dati in un nuovo redis, che verrà letto da event_stream() che a sua volta passerà al frontend
        #     #    I dati pubblicati devono avere tipo grafico, asse x e valori
            num=num+1
            print(str(num)+"<", end="")



        print("gia finito?")
        return 1

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