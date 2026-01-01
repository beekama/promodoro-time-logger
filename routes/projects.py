from flask import Blueprint, render_template, request, redirect, url_for
from services.projects import create_project

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            create_project(name)
        return redirect(url_for("projects.index"))

    return render_template("index.html")
