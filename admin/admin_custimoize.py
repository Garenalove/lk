from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask import redirect, url_for
from flask_admin import AdminIndexView
from database.models import Addon


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index.index'))


class AdminModelView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class AddonModelView(AdminMixin, ModelView):

    form_columns = ['name', 'description', 'cost', 'period']

    def on_model_change(self, form, model, is_created):
        if isinstance(model, Addon):
            model.generate_slug()
        return super(AddonModelView, self).on_model_change(form,model,is_created)


class UserModelView(AdminMixin, ModelView):
    form_columns = ['email', 'password', 'balance', 'roles', 'computers_limit']