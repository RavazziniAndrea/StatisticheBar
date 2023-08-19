import yaml

class ConfigReader:

    config_filename = "config.yml"

    def ConfigReader(self):
        with open(self.config_filename, 'r') as file:
            config = yaml.safe_load(file)

        db_address = config['db_address']
        db_name    = config['db_name']
        db_user    = config['db_user']
        db_passwd  = config['db_passwd']



# print(prime_service['prime_numbers'][0])
# print(prime_service['rest']['url'])