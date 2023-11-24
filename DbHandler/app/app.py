
import redis as Redis

import DatabaseUtils
from Exceptions import config_exception

redis = None

def publishData():
    print("redis")

def readCommonConfig():
    print("okokokok")

if __name__ == "__main__":
    readCommonConfig()
    redis = Redis.Redis(host="172.17.0.2", port="6379")
    