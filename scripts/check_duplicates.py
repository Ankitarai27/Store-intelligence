from app.db.session import engine
from sqlalchemy import text

QUERY = """
SELECT visitor_id, timestamp, event_type, COUNT(*)
FROM events
GROUP BY visitor_id, timestamp, event_type
HAVING COUNT(*) > 1;
"""

def check_duplicates():
    with engine.connect() as conn:
        result = conn.execute(text(QUERY)).fetchall()
        return result

if __name__ == "__main__":
    dupes = check_duplicates()

    if not dupes:
        print("✅ NO DUPLICATES FOUND")
    else:
        print("❌ DUPLICATES FOUND:")
        for d in dupes:
            print(d)