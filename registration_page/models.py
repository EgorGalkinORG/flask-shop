from project.settings import DATABASE
from flask_login import UserMixin

class User(DATABASE.Model, UserMixin):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)

    login = DATABASE.Column(DATABASE.String(25), nullable = False)
    email = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(20), nullable = False)
    is_admin = DATABASE.Column(DATABASE.Boolean)
    
    def __repr__(self) -> str:
        return f"login: {self.login}"
