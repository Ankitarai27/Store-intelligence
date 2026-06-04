from uuid import UUID

from app.models.anomaly import Anomaly
from app.repositories.anomaly import AnomalyRepository


class AnomalyService:
    def __init__(
        self,
        repository: AnomalyRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        anomaly: Anomaly,
    ) -> Anomaly:
        return self.repository.create_anomaly(anomaly)

    def get_by_store(
        self,
        store_id: UUID,
    ) -> list[Anomaly]:
        return self.repository.get_by_store(store_id)

    def get_open_anomalies(
        self,
        store_id: UUID,
    ) -> list[Anomaly]:
        return self.repository.get_open_anomalies(store_id)