
import redis as Redis
import time

import DatabaseUtils.database_handler as db_handler
import common_reader
from Exceptions import config_exception

redis = None

def publishData():
    db_handler.get_dati_db(redis)

if __name__ == "__main__":
    print("Avvio DbHandler", flush=True)
    redis = Redis.Redis(host=common_reader.redis_address, port=common_reader.redis_port)
    publishData()