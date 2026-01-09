from flask import Blueprint, render_template, request, redirect, url_for, session
from services.projects import create_project, get_projects_for_user

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
            return redirect(url_for("auth.login"))

    user_id = session["user"]["sub"]

    if request.method == "POST":
        name = request.form.get("name")
        if name:
            create_project(name, user_id)
        return redirect(url_for("projects.index"))

    projects = get_projects_for_user(user_id)
    return render_template("index.html", projects=projects)
