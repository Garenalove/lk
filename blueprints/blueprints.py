from server import server
from .shop_blueprint import shop_blueprint
from .index_blueprint import index_blueprint
from .account_blueprint import account_blueprint


def init_blueprints():
    server.register_blueprint(index_blueprint, url_prefix='/')
    server.register_blueprint(shop_blueprint, url_prefix='/shop')
    server.register_blueprint(account_blueprint,url_prefix='/account')