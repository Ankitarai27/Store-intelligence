from scripts.reset_db import reset_db
from scripts.replay_events import replay
from scripts.check_duplicates import check_duplicates
from scripts.validate_sessions import validate

def run():
    print("\n🚀 MILESTONE 4 STARTING...\n")

    # 1. RESET DB
    reset_db()

    # 2. REPLAY EVENTS
    print("\n📦 Replaying events...")
    results = replay()

    # 3. CHECK DUPLICATES
    print("\n🔍 Checking duplicates...")
    dupes = check_duplicates()

    # 4. VALIDATE SESSIONS
    print("\n🧠 Validating sessions...")
    sessions = validate()

    # 5. FINAL REPORT
    print("\n📊 FINAL REPORT")
    print("- Events processed:", len(results))
    print("- Duplicates found:", len(dupes))
    print("- Sessions:", len(sessions))

    print("\n✅ MILESTONE 4 COMPLETE")

if __name__ == "__main__":
    run()