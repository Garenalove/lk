from flask import Blueprint, render_template
from flask_security import current_user

index_blueprint = Blueprint('index', __name__, template_folder='templates')


@index_blueprint.route('/')
def index():
    return render_template('index/index.html')