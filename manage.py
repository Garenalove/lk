from server import manager
from database.models import Role

if __name__ == '__main__':
    from database.models import *
    manager.run()


def init_roles():
    if not Role.query.fillter(Role.name == 'admin').first():
        Role('admin').create()
