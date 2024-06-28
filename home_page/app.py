import flask

home_page = flask.Blueprint(
    name= "home",
    import_name= "app",
    template_folder= "home_page/templates",
    static_url_path= "/home/",
    static_folder="home_page/static"
)
