from flask import Flask
from routes.projects import projects_bp


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.register_blueprint(projects_bp)
    return app
