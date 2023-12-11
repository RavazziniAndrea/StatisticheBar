import json
import os
from Exceptions.config_exception import ConfigException


def valida_config(redis_address, redis_port):
    return \
        redis_address != "" and \
        redis_port    != ""

config_filename = os.path.abspath("common_config.json")
file = open(config_filename)
config = json.load(file)

redis_address = config['redis']['address']
redis_port    = config['redis']['port']

if(not valida_config(redis_address, redis_port)):
    raise ConfigException("Common config error")

