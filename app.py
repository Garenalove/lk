from index.blueprint import index_blueprint
from shop.blueprint import shop_blueprint
from account.blueprint import account_blueprint
from flask_security import SQLAlchemyUserDatastore, Security
from database.models import User, Role
from server import server, db
from admin.admin import init_admin


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(server, user_datastore)

init_admin()

server.register_blueprint(index_blueprint, url_prefix='/')
server.register_blueprint(shop_blueprint, url_prefix='/shop')
server.register_blueprint(account_blueprint,url_prefix='/account')

if __name__ == '__main__':
    server.run()