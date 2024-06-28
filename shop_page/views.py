import flask, flask_login
from project.settings import DATABASE
from registration_page.models import User
from .models import Product

value = 0
value_tf = False
def render_shop_page():
    global value_tf, value
    is_admin = False
    if flask.request.method == "POST":
        value += 1
        if not value_tf:
            value_tf = True
    is_admin = flask_login.current_user.is_admin

    return flask.render_template(
        template_name_or_list= "shop.html",
        user = flask_login.current_user.login,
        value1 = value,
        valuetf = value_tf,
        products = Product.query.all(),
        int = int,
        is_admin = is_admin
    )