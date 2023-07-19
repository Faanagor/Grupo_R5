from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DB_ENGINE = 'mysql'
DB_LIBRARY = 'pymysql'
DB_USER = 'root'
# DB_PASS = 'grupo_R5'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'bibliotecaDB'

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/bibliotecaDB"
SQLALCHEMY_DATABASE_URL = '{}+{}://{}@{}:{}/{}'.format(DB_ENGINE,
                                                       DB_LIBRARY,
                                                       DB_USER,
                                                       DB_HOST,
                                                       DB_PORT,
                                                       DB_NAME)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
