from authlib.integrations.flask_client import OAuth
import os

oauth = OAuth()

def init_keycloak(app):
    oauth.init_app(app)
    cfg = app.config

    oauth.register(
        name="keycloak",
        client_id=cfg["KEYCLOAK_CLIENT_ID"],
        client_secret=cfg["KEYCLOAK_CLIENT_SECRET"],
        server_metadata_url=(
            f'{cfg["KEYCLOAK_SERVER_URL"]}'
            f'/realms/{cfg["KEYCLOAK_REALM"]}'
            f'/.well-known/openid-configuration'
        ),
        client_kwargs={"scope": "openid profile email"},
    )
