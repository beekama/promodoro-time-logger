from flask import Flask
from routes.projects import projects_bp
from routes.auth import auth_bp
from auth.keycloak import init_keycloak
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_proto=1,
    x_host=1
)

def create_app():
    
    app.config.from_prefixed_env()


    # Initialize Extensions
    init_keycloak(app)

    app.register_blueprint(projects_bp)
    app.register_blueprint(auth_bp)

    return app
