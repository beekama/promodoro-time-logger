from db import get_connection

def create_project(name: str, owner_id: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO projects (name, owner_id) 
        VALUES (%s, %s)
        """,
        (name, owner_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_projects_for_user(owner_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, name, created_at 
        FROM projects 
        WHERE owner_id = %s
        ORDER BY created_at DESC
        """,
        (owner_id,)
    )
    projects = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "id": project[0],
            "name": project[1],
            "created_at": project[2],
        }
        for project in projects
    ]
