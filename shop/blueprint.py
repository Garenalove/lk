from flask import Blueprint, render_template, redirect, request
from database.queries import addons
from database.models import Product
from flask_security import current_user
from database.models import License, User
from server import db


shop_blueprint = Blueprint('shop', __name__, template_folder='templates')


@shop_blueprint.route('/')
def shop():
    return render_template('shop/shop.html', addons=addons())


@shop_blueprint.route('/<slug>', methods=['POST', 'GET'])
def addon_detail(slug):
    response = None
    license_ = None
    addon = Product.query.filter(Product.link == slug).first()
    if current_user.is_authenticated:
        license_ = current_user.is_addon(addon)
    if request.method == 'POST' and current_user.is_authenticated:
        if current_user.balance >= addon.cost and not license_:
            current_user.balance -= addon.cost
            license_ = License(addon)
            db.session.add(license_)
            db.session.commit()
            current_user.licenses.append(license_)
            db.session.add(current_user)
            db.session.commit()
            response = 'Покупка успешна совершена'
        else:
            response = 'Недостаточно срдеств для покупки'

    if addon:
        return render_template('shop/addon_detail.html', addon=addon, response=response, license_=license_)
    return redirect('/')
