import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

db = os.getenv("db")
database_url = db

engine = create_engine(database_url)

Session = sessionmaker(bind = engine)

Base = declarative_base()       