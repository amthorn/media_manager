import sys
import logging
import argparse
import os

from flask import Flask
from local_config import MYSQL_CONFIG, LOGGER_CONFIG, JSON_IMDB_IDS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
Base = declarative_base()


def setup_logger(level=logging.INFO):
    logger = logging.getLogger(LOGGER_CONFIG['NAME'])
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(logging.Formatter(LOGGER_CONFIG['FORMAT']))
    logger.addHandler(ch)
    logger.setLevel(level=level)
    logger.debug("Logger configured")
    return logger


def setup_alchemy():
    # Build sql engine
    engine = create_engine(
        'mysql+mysqldb://{}@{}/{}'.format(
            MYSQL_CONFIG['MYSQL_USER'],
            MYSQL_CONFIG['MYSQL_HOST'],
            MYSQL_CONFIG['MYSQL_DB']
        )
    )

    Base.metadata.bind = engine

    # SQL Session
    DBSession = sessionmaker()
    DBSession.bind = engine
    app.session = DBSession()
    return engine


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--reset', action='store_true')
    parser.add_argument('--level', type=str)

    return parser.parse_args()


def purge_tables():
    # delete databases
    from app import engine
    Base.metadata.drop_all(engine)

    # create the databases again
    Base.metadata.create_all(engine)
    app.session.commit()
    sys.exit(0)

def setup_artifacts():
    if not os.path.exists(JSON_IMDB_IDS):
        with open(JSON_IMDB_IDS, 'w') as file:
            file.write("[]")



args = parse_args()
logger = setup_logger(level=getattr(logging, args.level or 'INFO'))
engine = setup_alchemy()
setup_artifacts()

from app.sql.models import *  # noqa
from app.v1 import *  # noqa
from app.views import *  # noqa


if args.reset:
    purge_tables()
