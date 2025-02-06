from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv('DATABASE_URL')
# banco  = DATABASE_URL.split('/')[-1]

db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

Base.metadata.create_all(bind=db)
