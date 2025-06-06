import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
domain = config.get('DB', 'DOMAIN')
port = config.get('DB', 'PORT')
database = config.get('DB', 'DB_NAME')

SECRET_KEY = config.get("AUTH", "SECRET_KEY")

DB_URL = f"postgresql://{username}:{password}@{domain}:{port}/{database}"
