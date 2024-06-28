import flask

shop_page = flask.Blueprint(
    name= "shop",
    import_name= "app",
    template_folder= "shop_page/templates",
    static_url_path= "/shop/",
    static_folder="shop_page/static"
)
