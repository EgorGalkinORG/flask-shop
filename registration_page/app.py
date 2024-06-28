import flask

register_page = flask.Blueprint(
    name= "registration",
    import_name="app",
    template_folder= "registration_page/templates",
    static_url_path= "/registration/",
    static_folder="registration_page/static"
)