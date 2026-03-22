from flask import Blueprint, render_template, request, redirect, url_for, session
from services.projects import (
    create_project, 
    get_projects_for_user,
    start_time_log,
    stop_time_log,
    delete_project,
    get_running_projects,
    get_total_time_per_project
)

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
    running = get_running_projects(user_id)
    totals = get_total_time_per_project(user_id)
    
    return render_template(
        "index.html",
        projects=projects,
        running=running,
        totals=totals
    )

@projects_bp.post("/delete/<project_id>")
def delete(project_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    user_id = session["user"]["sub"]
    delete_project(project_id, user_id)

    return redirect(url_for("projects.index"))

@projects_bp.post("/start/<project_id>")
def start(project_id):
    user_id = session["user"]["sub"]

    try:
        start_time_log(project_id, user_id)
    except ValueError:
        pass  # optionally flash message

    return redirect(url_for("projects.index"))

@projects_bp.post("/stop/<project_id>")
def stop(project_id):
    user_id = session["user"]["sub"]

    try:
        stop_time_log(project_id, user_id)
    except ValueError:
        pass

    return redirect(url_for("projects.index"))
