import flask, flask_sqlalchemy, flask_migrate, os

project = flask.Flask(
    import_name="project",
    template_folder="templates",
    instance_path= os.path.abspath(__file__ + "/..")
)
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app= project)

migrate = flask_migrate.Migrate(app= project, db= DATABASE)
