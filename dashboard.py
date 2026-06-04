import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Store Intelligence Dashboard", layout="wide")

st.title("🛒 Store Intelligence Dashboard")

# ---------------------------
# HEALTH CHECK
# ---------------------------
st.header("System Status")

if st.button("Check API Health"):
    try:
        res = requests.get(f"{API_URL}/")
        st.success(res.json())
    except Exception as e:
        st.error(f"API not reachable: {e}")

# ---------------------------
# SEND EVENT
# ---------------------------
st.header("Send Event (Test Ingestion)")

visitor_id = st.text_input("Visitor ID", "v1")
store_id = st.text_input("Store ID", "s1")

event_type = st.selectbox(
    "Event Type",
    ["ENTRY", "EXIT", "ZONE_ENTER", "ZONE_EXIT", "BILLING_QUEUE_JOIN"]
)

camera_id = st.text_input("Camera ID", "cam-1")
zone_id = st.text_input("Zone ID", "zone-1")

if st.button("Send Event"):
    payload = {
        "visitor_id": visitor_id,
        "store_id": store_id,
        "event_type": event_type,
        "camera_id": camera_id,
        "zone_id": zone_id,
        "timestamp": "2026-06-04T10:00:00Z",
        "dwell_ms": 1200,
        "confidence": 0.95,
        "metadata_json": {}
    }

    try:
        res = requests.post(f"{API_URL}/events/ingest", json=payload)
        st.json(res.json())
    except Exception as e:
        st.error(e)

# ---------------------------
# SIMPLE ANALYTICS VIEW (MOCK)
# ---------------------------
st.header("Basic Analytics View")

st.info("This shows sample session analytics (replace with real endpoint later)")

data = pd.DataFrame([
    {"visitor": "v1", "session_time_sec": 120, "events": 5},
    {"visitor": "v2", "session_time_sec": 300, "events": 9},
    {"visitor": "v3", "session_time_sec": 45, "events": 2},
])

st.dataframe(data, use_container_width=True)

# ---------------------------
# EVENT FLOW SIMULATION
# ---------------------------
st.header("Event Flow Simulator")

if st.button("Run Demo Flow (ENTRY → EXIT)"):
    flow = [
        {"event_type": "ENTRY"},
        {"event_type": "ZONE_ENTER"},
        {"event_type": "BILLING_QUEUE_JOIN"},
        {"event_type": "EXIT"},
    ]

    results = []

    for e in flow:
        payload = {
            "visitor_id": "demo_user",
            "store_id": "store_1",
            "event_type": e["event_type"],
            "camera_id": "cam-1",
            "zone_id": "zone-A",
            "timestamp": "2026-06-04T10:00:00Z",
            "dwell_ms": 1000,
            "confidence": 0.99,
            "metadata_json": {}
        }

        r = requests.post(f"{API_URL}/events/ingest", json=payload)
        results.append(r.json())

    st.success("Flow executed")
    st.json(results)