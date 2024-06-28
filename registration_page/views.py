import flask
from .models import User
from project.settings import DATABASE
import flask_login

def render_registration():
    confirmed = False
    if flask.request.method == 'POST':
        

        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            is_admin = False
        )
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()

            confirmed = True
            # return flask.redirect("/login/")
        except:
            return "Не вдалося створити користувача"  
    print(confirmed)
    return flask.render_template(
        template_name_or_list='register.html', 
        show_confirmed = confirmed)