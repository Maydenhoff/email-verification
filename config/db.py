# from sqlalchemy import create_engine
# from sqlalchemy.orm.session import sessionmaker

# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/testdb"

# engine = create_engine(DATABASE_URL, echo=True)

# Session = sessionmaker(bind=engine)

# Base = declarative_base()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "postgresql://postgres:postgres@localhost:5432/testdb"

engine = create_engine(database_url)

Session = sessionmaker(bind = engine)

Base = declarative_base()