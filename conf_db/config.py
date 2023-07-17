import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('config.txt')

engine = create_engine("mysql+mysqlconnector://root:@localhost/users")
#engine = create_engine("mysql+mysqlconnector://zakaria:mirQwjTDedCHh9qpFSf80O4jVSDFLhvB@dpg-ci8f0h98g3nfuc833ltg-a.oregon-postgres.render.com/users_qmox")
#postgres://zakaria:mirQwjTDedCHh9qpFSf80O4jVSDFLhvB@dpg-ci8f0h98g3nfuc833ltg-a.oregon-postgres.render.com/users_qmox
#host = "viz-insight.mysql.database.azure.com"


