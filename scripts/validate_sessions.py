from app.db.session import engine
from sqlalchemy import text

QUERY = """
SELECT id, session_start, session_end
FROM visitors;
"""

def validate():
    with engine.connect() as conn:
        rows = conn.execute(text(QUERY)).fetchall()

    print("\nSESSION STATE:")
    for r in rows:
        print(r)

    return rows

if __name__ == "__main__":
    validate()