from flask import Blueprint, redirect, url_for, session, current_app
from auth.keycloak import oauth

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return oauth.keycloak.authorize_redirect(
        redirect_uri=url_for("auth.callback", _external=True)
    )

@auth_bp.route("/callback")
def callback():
    token = oauth.keycloak.authorize_access_token()
    session["user"] = token["userinfo"]
    return redirect("/")

@auth_bp.route("/logout")
def logout():
    session.clear()
    cfg = current_app.config

    return redirect(
        f'{cfg["KEYCLOAK_SERVER_URL"]}/realms/{cfg["KEYCLOAK_REALM"]}/protocol/openid-connect/logout'
        f'?client_id={cfg["KEYCLOAK_CLIENT_ID"]}'
        f'&post_logout_redirect_uri=https://plt.beekama.de/'
    )
