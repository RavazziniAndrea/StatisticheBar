import redis as Redis
import psycopg2
import time
from DatabaseUtils.dato_db import DatoDB
from DatabaseUtils.db_config_reader import DbConfigReader as conf 

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

# redis = None
# redis_instance = Redis.Redis(host="172.17.0.2", port="6379")

def get_dati_db(redis_instance):
    conn = None
    print("Connecting...")
    while conn is None:
        try:
            conn = prendi_connessione()
            time.sleep(1)
        except:
            pass
    print("...done")
    
#TODO gestire ciclo a monte se la connessione non si apre 
# o se viene chiusa per un errore

    try:
        cursor = conn.cursor()
        old_count = 0
        while not stop:
            cursor.execute(query)
            dati = cursor.fetchall()
            count = dati.__len__()
            if count != old_count:
                old_count = count
                print("Trovati nuovi record", flush=True)
                redis_instance.delete("datidb")
                list_dati = []
                for i in dati:
                    dato_db = DatoDB.parse_raw_data(i)

                    if dato_db is not None:
                        # print(str(dato_db.get_qta()) + " " + 
                        #     str(dato_db.get_tipo()) + " " +
                        #     str(dato_db.get_data()) + " " +
                        #     str(dato_db.get_ora()))
                        redis_instance.publish("datidb", str(dato_db.get_qta() ) + "#" + 
                                                str(dato_db.get_tipo()) + "#" +
                                                str(dato_db.get_data()) + "#" +
                                                str(dato_db.get_ora())  )
                        list_dati.append(dato_db)              
                redis_instance.publish("totaldb", str(list_dati.__len__()))
                print("total"+str(list_dati.__len__()), flush=True)
            time.sleep(2)

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