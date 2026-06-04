"""initial store intelligence schema

Revision ID: 20260530_000001
Revises: 
Create Date: 2026-05-30 00:00:01
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision: str = "20260530_000001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # =========================
    # ENUM TYPE
    # =========================
    event_type_enum = postgresql.ENUM(
        "ENTRY",
        "EXIT",
        "ZONE_ENTER",
        "ZONE_EXIT",
        "ZONE_DWELL",
        "BILLING_QUEUE_JOIN",
        "BILLING_QUEUE_ABANDON",
        "REENTRY",
        name="event_type_enum",
        create_type=False,
    )

    event_type_enum.create(op.get_bind(), checkfirst=True)
    # =========================
    # STORES
    # =========================
    op.create_table(
        "stores",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("city", sa.String(length=255), nullable=False),
        sa.Column("timezone", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index("ix_stores_name", "stores", ["name"])
    op.create_index("ix_stores_city", "stores", ["city"])

    # =========================
    # VISITORS
    # =========================
    op.create_table(
        "visitors",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "store_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("stores.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("is_staff", sa.Boolean(), nullable=False),
        sa.Column("session_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("session_end", sa.DateTime(timezone=True), nullable=True),
        sa.Column("is_converted", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index("ix_visitors_store_id", "visitors", ["store_id"])
    op.create_index("ix_visitors_session_start", "visitors", ["session_start"])

    # =========================
    # EVENTS
    # =========================
    op.create_table(
        "events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "visitor_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("visitors.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "store_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("stores.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "event_type",
            event_type_enum,
            nullable=False,
        ),
        sa.Column("camera_id", sa.String(length=128), nullable=False),
        sa.Column("zone_id", sa.String(length=128), nullable=True),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("dwell_ms", sa.Integer(), nullable=True),
        sa.Column("confidence", sa.Numeric(5, 4), nullable=False),
        sa.Column("metadata_json", postgresql.JSONB(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index(
        "ix_events_store_timestamp",
        "events",
        ["store_id", "timestamp"],
    )
    op.create_index(
        "ix_events_visitor_timestamp",
        "events",
        ["visitor_id", "timestamp"],
    )
    op.create_index("ix_events_event_type", "events", ["event_type"])
    op.create_index("ix_events_zone_id", "events", ["zone_id"])
    op.create_index("ix_events_camera_id", "events", ["camera_id"])

    # =========================
    # TRANSACTIONS
    # =========================
    op.create_table(
        "transactions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "visitor_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("visitors.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "store_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("stores.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("basket_value", sa.Numeric(12, 2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index(
        "ix_transactions_store_timestamp",
        "transactions",
        ["store_id", "timestamp"],
    )
    op.create_index(
        "ix_transactions_visitor_id",
        "transactions",
        ["visitor_id"],
    )

    # =========================
    # ANOMALIES
    # =========================
    op.create_table(
        "anomalies",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "store_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("stores.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("anomaly_type", sa.String(length=128), nullable=False),
        sa.Column("severity", sa.String(length=32), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=False),
        sa.Column("detected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("resolved_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index(
        "ix_anomaly_store_detected",
        "anomalies",
        ["store_id", "detected_at"],
    )
    op.create_index("ix_anomaly_type", "anomalies", ["anomaly_type"])
    op.create_index("ix_anomaly_severity", "anomalies", ["severity"])


def downgrade() -> None:
    # Drop in reverse order (dependency-safe)

    op.drop_index("ix_anomaly_severity", table_name="anomalies")
    op.drop_index("ix_anomaly_type", table_name="anomalies")
    op.drop_index("ix_anomaly_store_detected", table_name="anomalies")
    op.drop_table("anomalies")

    op.drop_index("ix_transactions_visitor_id", table_name="transactions")
    op.drop_index("ix_transactions_store_timestamp", table_name="transactions")
    op.drop_table("transactions")

    op.drop_index("ix_events_camera_id", table_name="events")
    op.drop_index("ix_events_zone_id", table_name="events")
    op.drop_index("ix_events_event_type", table_name="events")
    op.drop_index("ix_events_visitor_timestamp", table_name="events")
    op.drop_index("ix_events_store_timestamp", table_name="events")
    op.drop_table("events")

    op.drop_index("ix_visitors_session_start", table_name="visitors")
    op.drop_index("ix_visitors_store_id", table_name="visitors")
    op.drop_table("visitors")

    op.drop_index("ix_stores_city", table_name="stores")
    op.drop_index("ix_stores_name", table_name="stores")
    op.drop_table("stores")

    event_type_enum = postgresql.ENUM(name="event_type_enum")
    event_type_enum.drop(op.get_bind(), checkfirst=True)