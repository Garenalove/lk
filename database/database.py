import os
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from server import db as Base

config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
with open(config_path, 'r') as yaml_file:
    config = yaml.load(yaml_file).get('database')

session = Base.session
Base.query = session.query_property()

