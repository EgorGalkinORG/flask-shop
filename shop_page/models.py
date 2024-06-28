from project.settings import DATABASE


class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    name = DATABASE.Column(DATABASE.String(50), primary_key = False)
    price = DATABASE.Column(DATABASE.Integer, primary_key = False)
    discount = DATABASE.Column(DATABASE.Integer, primary_key = False)
    capacity1 = DATABASE.Column(DATABASE.String(20), primary_key = False)
    capacity2 = DATABASE.Column(DATABASE.String(20), primary_key = False)
    capacity3 = DATABASE.Column(DATABASE.String(20), primary_key = False)

    def __repr__(self):
        return f"id: {self.id}; name: {self.name};"