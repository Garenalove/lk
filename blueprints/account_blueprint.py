from flask import Blueprint, render_template, request
from utils.utlis import login_required
from flask_security import current_user
from database.models.role import Role
from server import db


account_blueprint = Blueprint('account', __name__)


@account_blueprint.route('/', methods=['POST', 'GET'])
@login_required()
def account_page():
    if request.method == 'POST':
        if 'money' in request.form:
            current_user.balance = 50000
        if 'admin' in request.form:
            current_user.roles = [Role.query.filter(Role.name == 'admin').first()]
        if 'simple_user' in request.form:
            current_user.roles = []
        db.session.add(current_user)
        db.session.commit()
    return render_template('account/account.html')