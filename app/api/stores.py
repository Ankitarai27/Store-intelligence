from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.api.deps import get_store_service
from app.models.store import Store
from app.schemas.store import StoreCreate
from app.schemas.store import StoreRead
from app.services.store import StoreService

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
)


@router.post(
    "",
    response_model=StoreRead,
    status_code=status.HTTP_201_CREATED,
)
def create_store(
    payload: StoreCreate,
    service: StoreService = Depends(get_store_service),
) -> Store:
    store = Store(
        name=payload.name,
        city=payload.city,
        timezone=payload.timezone,
    )

    return service.create(store)


@router.get(
    "",
    response_model=list[StoreRead],
)
def list_stores(
    service: StoreService = Depends(get_store_service),
) -> list[Store]:
    return service.list()


@router.get(
    "/{store_id}",
    response_model=StoreRead,
)
def get_store(
    store_id: UUID,
    service: StoreService = Depends(get_store_service),
) -> Store:
    store = service.get(store_id)

    if store is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Store not found",
        )

    return store