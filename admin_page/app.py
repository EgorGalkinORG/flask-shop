import flask

admin_page = flask.Blueprint(
    name= "admin",
    import_name= "admin_page",
    template_folder= "templates",
    static_url_path= "/admin/",
    static_folder="static"
)
