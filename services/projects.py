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
