import json
from os import path

class ConfigReader:

    config_filename = path.abspath("app/config/config.json")
    db_address = ""
    db_name    = ""
    db_user    = ""
    db_passwd  = ""
    
    def __init__(self):
        file = open(self.config_filename)
        config = json.load(file)

        self.db_address = config['database']['db_address']
        self.db_name    = config['database']['db_name']
        self.db_user    = config['database']['db_user']
        self.db_passwd  = config['database']['db_passwd']


    def valida_config(self):
        return \
            self.db_address != "" and \
            self.db_name    != "" and \
            self.db_user    != "" and \
            self.db_passwd  != ""


# print(prime_service['prime_numbers'][0])
# print(prime_service['rest']['url'])