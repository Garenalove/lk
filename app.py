from flask_security import SQLAlchemyUserDatastore, Security
from blueprints import init_blueprints
from admin.admin import init_admin
from database.models import User, Role
from server import server, db


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(server, user_datastore)

init_admin()

init_blueprints()

if __name__ == '__main__':
    server.run()