import os
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from server import db as Base

config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
with open(config_path, 'r') as yaml_file:
    config = yaml.load(yaml_file).get('database')

engine = create_engine(
    'postgresql://{user}:{password}@{address}:{port}/{name}'.format(
        user=config.get('user'),
        password=config.get('password'),
        address='localhost',
        port=5432,
        name=config.get('name', 'avspam'),
    ),
    convert_unicode=True
)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = session.query_property()

