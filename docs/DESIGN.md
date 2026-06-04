
---

## 2. DESIGN.md

```md
# System Design – Store Intelligence System

---

## Architecture Overview

- FastAPI handles API layer and business logic
- PostgreSQL stores structured retail event data
- SQLAlchemy provides ORM abstraction
- Alembic manages schema migrations
- Streamlit provides interactive simulation dashboard

---

## Event Ingestion Flow

1. Client sends event to `/events/ingest`
2. FastAPI validates request using Pydantic
3. EventService processes event
4. EventRepository checks deduplication
5. If not duplicate → event stored in PostgreSQL
6. VisitorService updates session state
7. TransactionService updates conversion status if needed
8. Response returned to client

---

## Sessionization Logic

- Visitor session starts on ENTRY event
- session_start set at first ENTRY
- session_end set on EXIT event
- If EXIT missing → session remains open (timeout placeholder)

---

## Deduplication Strategy

- Unique constraint:
  visitor_id + timestamp + event_type
- Checked at repository level before insertion
- Prevents duplicate ingestion from retries or replay

---

## Database Schema Overview

- stores → store metadata
- visitors → session tracking
- events → raw event stream
- transactions → purchase events
- anomalies → detected issues

---

## Technology Choices

### FastAPI
- High performance async API framework
- Easy integration with Pydantic

### PostgreSQL
- Reliable relational storage
- Strong indexing for event queries

### Streamlit
- Fast UI for simulation and demo
- No frontend overhead

---

## Data Flow
Streamlit / Client
    ↓
FastAPI /events/ingest
    ↓
EventService
    ↓
EventRepository → PostgreSQL
    ↓
VisitorService (session update)
    ↓
TransactionService (conversion update)
    ↓
Response