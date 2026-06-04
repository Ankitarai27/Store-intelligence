from app.db.session import engine
from sqlalchemy import text

def reset_db():
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE"))
        conn.execute(text("CREATE SCHEMA public"))

if __name__ == "__main__":
    reset_db()
    print("✅ DB RESET COMPLETE")