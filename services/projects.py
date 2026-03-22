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

def start_time_log(project_id: str, owner_id: str):
    conn = get_connection()
    cur = conn.cursor()

    # check no open time log
    cur.execute(
        """
        SELECT 1 FROM project_time_logs
        WHERE project_id = %s
        AND owner_id = %s
        AND ended_at IS NULL
        """,
        (project_id, owner_id)
    )

    if cur.fetchone():
        raise ValueError("Time tracking is already running for this project")
    
    cur.execute(
        """
        INSERT INTO project_time_logs (project_id, owner_id)
        VALUES (%s, %s)
        """,
        (project_id, owner_id)
    )

    conn.commit()
    cur.close()
    conn.close()

def stop_time_log(project_id: str, owner_id: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE project_time_logs
        SET ended_at = now()
        WHERE project_id = %s
        AND owner_id = %s
        AND ended_at IS NULL
        """,
        (project_id, owner_id)
    )

    if cur.rowcount == 0:
        raise ValueError("No running time log found")

    conn.commit()
    cur.close()
    conn.close()

def get_time_logs_for_project(project_id: str, owner_id: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, started_at, ended_at,
            EXTRACT(EPOCH FROM (ended_at - started_at)) AS duration_seconds
        FROM project_time_logs
        WHERE project_id = %s
        AND owner_id = %s
        ORDER BY started_at DESC
        """,
        (project_id, owner_id)
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "id": r[0],
            "started_at": r[1],
            "ended_at": r[2],
            "duration_seconds": r[3],
        }
        for r in rows
    ]
