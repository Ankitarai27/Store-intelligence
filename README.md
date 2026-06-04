# Store Intelligence System

A real-time retail event ingestion and analytics backend built with FastAPI, PostgreSQL, SQLAlchemy, and Streamlit dashboard for simulation and visualization.

---

## Tech Stack

- FastAPI (Backend API)
- PostgreSQL (Database)
- SQLAlchemy 2.0 (ORM)
- Alembic (Migrations)
- Pydantic v2 (Validation)
- Streamlit (Dashboard UI)
- Docker (Deployment)

---

## Features

- Real-time retail event ingestion
- Event types: ENTRY, EXIT, ZONE_ENTER, ZONE_EXIT, BILLING_QUEUE_JOIN
- Visitor session tracking
- Event deduplication (visitor_id + timestamp + event_type)
- Transaction conversion tracking
- Anomaly logging system
- RESTful APIs for stores, events, transactions, anomalies
- Streamlit-based event simulator dashboard

---

## Architecture Overview

FastAPI handles event ingestion and business logic.  
PostgreSQL stores structured retail data.  
SQLAlchemy manages ORM mapping.  
Streamlit provides a simulation and monitoring UI.  

---

## API Endpoints

### Stores
- POST /stores
- GET /stores
- GET /stores/{store_id}

### Events
- POST /events/ingest
- POST /events/ingest/bulk

### Transactions
- POST /transactions
- GET /transactions

### Anomalies
- POST /anomalies
- GET /anomalies

---

## How to Run

### 1. Clone project
```bash
git clone <repo_url>
cd store-intelligence
```

### 2. Start services
```bash
docker-compose up --build
```

### 3. Run migrations
```bash
alembic upgrade head
```

### 4. Start backend
```bash
uvicorn app.main:app --reload
```


## Run Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```

 ## Example API Request
 ```bash 
POST /events/ingest
{
  "visitor_id": "b1a3c2d4-1111-2222-3333-abcdef123456",
  "store_id": "a9f8c7d6-9999-8888-7777-abcdef654321",
  "event_type": "ENTRY",
  "camera_id": "CAM_01",
  "zone_id": "ZONE_A",
  "timestamp": "2026-06-04T10:00:00Z",
  "dwell_ms": null,
  "confidence": 0.98,
  "metadata_json": {
    "device": "camera_v2"
  }
}
```

### Expected Output
```bash
{
  "status": "processed",
  "event_id": "uuid-generated-id"
}
```


## Folder Structure
```
app/
    ├── api/
    ├── core/
    ├── db/
    ├── models/
    ├── repositories/
    ├── schemas/
    ├── services/
    ├── main.py
dashboard/
    ├── app.py
alembic/
```