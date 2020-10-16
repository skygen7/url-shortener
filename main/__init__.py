from flask import Flask
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import load_config

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.secret_key = 'hard to guess string'

engine = create_engine(load_config())
Session = sessionmaker(bind=engine)
session = Session()

import main.views
