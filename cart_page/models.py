from project.settings import DATABASE


class Cart(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    
    name = DATABASE.Column(DATABASE.Text, primary_key = False)
    surname = DATABASE.Column(DATABASE.Text, primary_key = False)
    phone_number = DATABASE.Column(DATABASE.Integer, primary_key = False)
    email = DATABASE.Column(DATABASE.Text, primary_key = False)
    city = DATABASE.Column(DATABASE.Text, primary_key = False)
    wishes = DATABASE.Column(DATABASE.Text, primary_key = False)
    cart = DATABASE.Column(DATABASE.Text, primary_key = False)
    status = DATABASE.Column(DATABASE.Text, primary_key = False)
    
    def __repr__(self):
        return f"id: {self.id}; name: {self.login}"