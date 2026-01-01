from flask import Flask
from routes.projects import projects_bp

app = Flask(__name__)

def create_app():
    app.register_blueprint(projects_bp)
    return app
