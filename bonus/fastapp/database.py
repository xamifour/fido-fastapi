import databases
from sqlalchemy import create_engine, MetaData


DATABASE_URL = "sqlite:///../transactions.sqlite"

database = databases.Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
