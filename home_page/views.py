import flask
from flask_login import current_user

from registration_page.models import User
is_admin = False
def render_home_page():
    global is_admin
    try:
        user1 = current_user.login
    except Exception as e:
        print(e)
        user1 = "1"
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    return flask.render_template(
        template_name_or_list= "home.html",
        is_auth = current_user.is_authenticated,
        user = user1, is_admin = is_admin
    )   