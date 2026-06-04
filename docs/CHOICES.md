# CHOICES

# Engineering Decisions – Store Intelligence System

---

## Event-Driven Architecture

Chosen because retail behavior is naturally sequential and time-based. Events represent real-world actions.

---

## SQLAlchemy + PostgreSQL

- Strong relational consistency
- Efficient indexing for time-series queries
- Mature ORM ecosystem

---

## UUID-Based Deduplication

- Ensures global uniqueness
- Prevents replay ingestion issues
- Works well in distributed systems

---

## Backend Sessionization

Session logic is handled server-side to ensure:
- Consistency across devices
- Reliable analytics
- No client trust dependency

---

## Repository Pattern

- Separates business logic from DB layer
- Improves testability
- Keeps service layer clean

---

## Streamlit for Dashboard

- Rapid UI development
- Ideal for demo purposes
- No frontend engineering overhead

---

## Tradeoffs

- No caching layer (Redis omitted)
- No message queue (Kafka/RabbitMQ not used)
- Basic session timeout not implemented
- Minimal anomaly detection logic

---

## Production Improvements

- Add Kafka for event streaming
- Introduce Redis caching layer
- Add async worker for ingestion
- Implement real-time analytics dashboard
- Add observability (Prometheus + Grafana)


4. CLEAN PROJECT CODE SUMMARY
# Final Project Structure

```
app/
├── api/
│ ├── deps.py → Dependency injection (DB, services)
│ ├── events.py → Event ingestion endpoints
│ ├── stores.py → Store CRUD APIs
│ ├── transactions.py → Transaction APIs
│ ├── anomalies.py → Anomaly APIs
│ └── health.py → Health check endpoint
│
├── core/
│ ├── config.py → App settings
│ ├── logging.py → Logging setup
│
├── db/
│ ├── session.py → PostgreSQL session manager
│ ├── base.py → SQLAlchemy base
│
├── models/
│ ├── store.py → Store entity
│ ├── visitor.py → Visitor sessions
│ ├── event.py → Event stream
│ ├── transaction.py → Purchase data
│ ├── anomaly.py → Anomaly tracking
│ ├── enums.py → EventType enum
│
├── repositories/
│ ├── base.py → Generic repository
│ ├── store.py → Store DB operations
│ ├── event.py → Event DB operations
│ ├── visitor.py → Visitor queries
│ ├── transaction.py → Transaction queries
│ ├── anomaly.py → Anomaly queries
│
├── schemas/
│ ├── store.py → Store request/response schemas
│ ├── event.py → Event ingestion schemas
│ ├── transaction.py → Transaction schemas
│ ├── anomaly.py → Anomaly schemas
│ ├── common.py → Pagination models
│
├── services/
│ ├── store.py → Store business logic
│ ├── event.py → Event ingestion logic
│ ├── visitor.py → Session management
│ ├── transaction.py → Conversion tracking
│ ├── anomaly.py → Anomaly handling
│
├── main.py → FastAPI app entrypoint

dashboard/
├── app.py → Streamlit simulation UI

alembic/
├── versions/ → DB migrations

```

---

## Key Files

- main.py → App entrypoint
- api/events.py → Event ingestion API
- services/event.py → Core ingestion logic
- services/visitor.py → Session tracking
- repositories/ → Database access layer
- schemas/ → API validation layer
- models/ → Database schema definitions

---

## System Summary

- Event-driven retail intelligence backend
- Session tracking + conversion detection
- Deduplicated event ingestion pipeline
- PostgreSQL-backed analytics-ready structure
- Streamlit simulation dashboard for demo