from flask import Flask
import os
import yaml
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(config_path, 'r') as yaml_file:
    config = yaml.load(yaml_file)

server = Flask(__name__)
server.config.update(config.get('server'))


db = SQLAlchemy(server)
migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command('db', MigrateCommand)

