import requests
from scripts.seed_events import get_events

URL = "http://127.0.0.1:8000/events/ingest"

def replay():
    results = []

    for event in get_events():
        r = requests.post(URL, json=event)
        results.append(r.json())

    return results

if __name__ == "__main__":
    print(replay())