import redis
import psycopg2
from config_reader import ConfigReader as conf


def publica_dati_sse():
    conn = None
    try:
        conn = prendi_connessione()
        cursor = conn.cursor()
        
        cursor.execute("SELECT r.quantita AS qta, r.descrizione AS tipo FROM ordini ord JOIN righe r ON ord.id = r.id_ordine JOIN righe_articoli ra ON r.id = ra.id_riga WHERE ra.desc_tipologia = 'alcool' OR ra.desc_tipologia = 'super'")
        for i in cursor.fetchall():
            print(i)
    
    # close the communication with the PostgreSQL
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
