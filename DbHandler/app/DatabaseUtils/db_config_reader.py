import json
import os
from Exceptions.config_exception import ConfigException

class DbConfigReader:

    def valida_config(db_address, db_name, db_user, db_passwd):
        return \
            db_address != "" and \
            db_name    != "" and \
            db_user    != "" and \
            db_passwd  != ""

    config_filename = os.path.abspath("db_config.json")
    file = open(config_filename)
    config = json.load(file)

    db_address = config['database']['db_address']
    db_name    = config['database']['db_name']
    db_user    = config['database']['db_user']
    db_passwd  = config['database']['db_passwd']

    if(not valida_config(db_address, db_name, db_user, db_passwd)):
        raise ConfigException("Database config error")
