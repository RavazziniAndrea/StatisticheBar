import redis as Redis


redis = Redis.Redis(host="172.17.0.2", port="6379")

class RedisPublisher:

    @staticmethod
    def leggi_e_pubblica():
        print("leggo e pubblico")
        pubsub = redis.pubsub()
        pubsub.subscribe("datidb")
        num=0
        for datodb in pubsub.listen():
            
            
        #     #TODO in questo punto ottengo tutti i dati dal db. 
        #     # 1. Parsare i dati in record (dato_db.py)
        #     # 2. Creare le aggregazioni in base al grafico richiesto
        #     # 3. Pubblicare i dati in un nuovo redis, che verrà letto da event_stream() che a sua volta passerà al frontend
        #     #    I dati pubblicati devono avere tipo grafico, asse x e valori
            num=num+1
            print(str(num)+"<", end="")



        print("gia finito?")
        return 1
