from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.anomaly import Anomaly
from app.repositories.base import BaseRepository


class AnomalyRepository(BaseRepository[Anomaly]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Anomaly)

    def create_anomaly(self, anomaly: Anomaly) -> Anomaly:
        return self.create(anomaly)

    def get_open_anomalies(self, store_id: UUID) -> list[Anomaly]:
        stmt = select(Anomaly).where(
            Anomaly.store_id == store_id,
            Anomaly.resolved_at.is_(None),
        )

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def get_by_store(self, store_id: UUID) -> list[Anomaly]:
        stmt = select(Anomaly).where(Anomaly.store_id == store_id)

        result = self.session.execute(stmt)

        return list(result.scalars().all())