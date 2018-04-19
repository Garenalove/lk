from flask_admin import Admin
from server import server
from database.models import *
from database.database import session
from flask_admin.contrib.sqla import ModelView
from .admin_custimoize import UserModelView, AddonModelView, HomeAdminView


def init_admin():
    admin = Admin(server, 'Admin', index_view=HomeAdminView(name='Home'))
    admin.add_view(UserModelView(User, session))
    admin.add_view(AddonModelView(Addon, session))
    admin.add_view(ModelView(Role, session))

