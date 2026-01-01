from db import get_connection

def create_project(name: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projects (name) VALUES (%s)",
        (name,)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_all_projects():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, created_at FROM projects ORDER BY created_at DESC"
    )
    projects = cur.fetchall()
    cur.close()
    conn.close()
    return projects

