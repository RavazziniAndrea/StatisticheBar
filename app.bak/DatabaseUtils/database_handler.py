import redis as Redis
import psycopg2
import time
from DatabaseUtils.dato_db import DatoDB
from config_reader import ConfigReader as conf 

query="""
SELECT r.quantita AS qta, r.descrizione AS tipo, ord.data as data, ord.ora as ora 
FROM ordini ord 
JOIN righe r ON ord.id = r.id_ordine 
JOIN righe_articoli ra ON r.id = ra.id_riga 
WHERE ord.data IS NOT NULL 
AND ord.ora IS NOT NULL 
AND (ra.desc_tipologia = 'alcool' 
OR ra.desc_tipologia = 'super')
ORDER BY ord.data ASC, ord.ora ASC"""

stop = False

redis = Redis.Redis(host="172.17.0.2", port="6379")
# redis = Redis.Redis(host="172.18.0.2", port="6379")

def get_dati_db():
    conn = None
    try:
        conn = prendi_connessione()
        cursor = conn.cursor()
        print("flusho")
        redis.flushall()
        old_count = 0
        global stop 
        stop = False
        while not stop:

            cursor.execute(query)
            dati = cursor.fetchall()

            count = dati.__len__
            if count != old_count:
                old_count = count
                list_dati = []
                for i in dati:
                    dato_db = DatoDB.parse_raw_data(i)
                    if dato_db is not None:
                        # print(str(dato_db.get_qta()) + " " + 
                        #     str(dato_db.get_tipo()) + " " +
                        #     str(dato_db.get_data()) + " " +
                        #     str(dato_db.get_ora()))
                        redis.publish("datidb", "dato_db.__str__()")
                        list_dati.append(dato_db)
                    #TODO, check che i dati precedenti vengano effettivamente tolti, se no ci si trova con mille dati su redis 
                
                redis.publish("totaldb", str(list_dati.__len__()))

                print("bastaaaaa"+str(list_dati.__len__()))
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