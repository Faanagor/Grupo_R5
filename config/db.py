from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker
import pymysql


pymysql.install_as_MySQLdb()
DB_USER = 'root'
DB_PASS = 'grupo_R5'
DB_HOST = 'localhost'
DB_PORT = '3306'
DATABASE = 'new_db_biblioteca'
TIMEOUT = '?connect_timeout=60'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:grupo_R5@localhost:3306/bibliotecaDB"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
conn = engine.connect()
# engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USER,
#                                                                   DB_PASS,
#                                                                   DB_HOST,
#                                                                   DB_PORT,
#                                                                   DATABASE,
#                                                                   TIMEOUT)


meta = MetaData()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
