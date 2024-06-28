import flask

cart_page = flask.Blueprint(
    name= "cart",
    import_name= "app",
    template_folder= "cart_page/templates",
    static_url_path= "/cart/",
    static_folder="cart_page/static"
)
