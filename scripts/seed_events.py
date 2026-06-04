from uuid import uuid4
from datetime import datetime, timedelta

def get_events():
    base_time = datetime.utcnow()

    return [
        {
            "event_id": str(uuid4()),
            "store_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "visitor_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "event_type": "ENTRY",
            "camera_id": "cam-1",
            "timestamp": base_time.isoformat(),
            "confidence": 0.98
        },
        {
            "event_id": str(uuid4()),
            "store_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "visitor_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "event_type": "ZONE_ENTER",
            "camera_id": "cam-1",
            "zone_id": "cosmetics",
            "timestamp": (base_time + timedelta(minutes=1)).isoformat(),
            "confidence": 0.95
        },
        {
            "event_id": str(uuid4()),
            "store_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "visitor_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "event_type": "BILLING_QUEUE_JOIN",
            "camera_id": "cam-2",
            "timestamp": (base_time + timedelta(minutes=5)).isoformat(),
            "confidence": 0.97
        },
        {
            "event_id": str(uuid4()),
            "store_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "visitor_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "event_type": "EXIT",
            "camera_id": "cam-1",
            "timestamp": (base_time + timedelta(minutes=10)).isoformat(),
            "confidence": 0.99
        },

        # DUPLICATE ENTRY TEST
        {
            "event_id": "DUPLICATE-ENTRY",
            "store_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "visitor_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
            "event_type": "ENTRY",
            "camera_id": "cam-1",
            "timestamp": base_time.isoformat(),
            "confidence": 0.98
        }
    ]