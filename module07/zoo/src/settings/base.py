import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

HASH_ALGORITHM = config.get("AUTH", "HASH_ALGORITHM", fallback="HS256")
HASH_SECRET = config.get("AUTH", "HASH_SECRET")
DB_NAME = config.get("DB", "DB_NAME", fallback="db")
