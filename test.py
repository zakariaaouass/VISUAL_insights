from sqlalchemy import create_engine

# Set the Azure MySQL credentials directly
username = 'zakaria'
password = 'Zamla7iti3robia@'
hostname = 'viz-insight.mysql.database.azure.com'
database = 'users'
ssl_ca = 'DigiCertGlobalRootCA.crt'

connection_url = "mysql+mysqlconnector://"+username+":"+password+"@"+hostname+"/"+database+"?ssl_ca="+ssl_ca

# Create the SQLAlchemy engine
engine = create_engine(connection_url)

# Test the connection
try:
    with engine.connect() as connection:
        print('Connected to Azure MySQL!')
        version = connection.execute('SELECT VERSION()').fetchone()
        print(f'Database version: {version[0]}')
except Exception as e:
    print(f'Error connecting to Azure MySQL: {e}')
