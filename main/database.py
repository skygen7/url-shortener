from sqlalchemy import Text, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from main.settings import load_config
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    real_url = Column(Text, unique=True)
    hash_url = Column(Text)
    count = Column(Integer)

    def __init__(self, real_url, hash_url, count):
        self.real_url = real_url
        self.hash_url = hash_url
        self.count = count

    def __repr__(self):
        return f"<Urls({self.real_url},{self.hash_url}, {self.count})>"


engine = create_engine(load_config().get('db_parameters'))

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
