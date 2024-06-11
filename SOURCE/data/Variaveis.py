import configparser

config = configparser.ConfigParser()
config.read('config.ini')

email = config['credenciais']['email']
senha = config['credenciais']['senha']
