import redis as Redis
import psycopg2
import time
from config_reader import ConfigReader as conf 

query="SELECT r.quantita AS qta, r.descrizione AS tipo, ord.data as data, ord.ora as ora FROM ordini ord JOIN righe r ON ord.id = r.id_ordine JOIN righe_articoli ra ON r.id = ra.id_riga WHERE ra.desc_tipologia = 'alcool' OR ra.desc_tipologia = 'super'"

stop = False

# redis = Redis.Redis(host="172.17.0.2", port="6379")
redis = Redis.Redis(host="172.18.0.2", port="6379")

def get_dati_db():
    conn = None
    try:
        conn = prendi_connessione()
        cursor = conn.cursor()

        old_count = 0
        while not stop:

            cursor.execute(query)
            dati = cursor.fetchall()

            count = dati.__len__
            if count != old_count:
                old_count = count
                for i in dati:
                    redis.publish("datidb", str(i))
                    #TODO, check che i dati precedenti vengano effettivamente tolti, se no ci si trova con mille dati su redis 
            time.sleep(3000)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def prendi_connessione():
    return psycopg2.connect(host     = conf.db_address,
                            database = conf.db_name,
                            user     = conf.db_user,
                            password = conf.db_passwd)

def stop_query():
    global stop
    stop = True

    # def getDatiDB():  
    #     print("Dentro thread")
    #     count = 0
    #     global stop
    #     stop = False
    #     while not stop:
    #         if(count > 100): count = 0
    #         count = count+1
    #         redis.publish("datidb", count)
    #         sleep(1)
    #     print("Fine thread")
