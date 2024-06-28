import flask, flask_login
from registration_page.models import User

def render_login_page():
    if flask.request.method == "POST":
        for user in User.query.filter_by(login = flask.request.form['login']):
            
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect('/')
        return "невірний пароль"
    return flask.render_template('login.html')
