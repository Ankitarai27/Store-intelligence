from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.api.deps import get_anomaly_service
from app.models.anomaly import Anomaly
from app.schemas.anomaly import AnomalyCreate
from app.schemas.anomaly import AnomalyRead
from app.services.anomaly import AnomalyService

router = APIRouter(
    prefix="/anomalies",
    tags=["Anomalies"],
)


@router.post(
    "",
    response_model=AnomalyRead,
)
def create_anomaly(
    payload: AnomalyCreate,
    service: AnomalyService = Depends(
        get_anomaly_service,
    ),
) -> Anomaly:
    anomaly = Anomaly(
        store_id=payload.store_id,
        anomaly_type=payload.anomaly_type,
        severity=payload.severity,
        description=payload.description,
        detected_at=payload.detected_at,
        resolved_at=payload.resolved_at,
    )

    return service.create(anomaly)


@router.get(
    "",
    response_model=list[AnomalyRead],
)
def list_anomalies(
    store_id: UUID,
    service: AnomalyService = Depends(
        get_anomaly_service,
    ),
) -> list[Anomaly]:
    return service.get_by_store(store_id)