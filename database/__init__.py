from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_URI
from .models import Base

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)