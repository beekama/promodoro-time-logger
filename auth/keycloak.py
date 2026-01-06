from authlib.integrations.flask_client import OAuth
import os

oauth = OAuth()

def init_keycloak(app):
    oauth.init_app(app)

    oauth.register(
        name="keycloak",
        client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
        client_secret=os.getenv("KEYCLOAK_CLIENT_SECRET"),
        server_metadata_url=(
            f'{os.getenv("KEYCLOAK_SERVER_URL")}'
            f'/realms/{os.getenv("KEYCLOAK_REALM")}'
            f'/.well-known/openid-configuration'
        ),
        client_kwargs={"scope": "openid profile email"},
    )
