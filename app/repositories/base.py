from __future__ import annotations

from typing import Generic
from typing import TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.base import Base

ModelT = TypeVar("ModelT", bound=Base)


class BaseRepository(Generic[ModelT]):
    def __init__(
        self,
        session: Session,
        model: type[ModelT],
    ) -> None:
        self.session = session
        self.model = model

    def create(self, instance: ModelT) -> ModelT:
        self.session.add(instance)
        self.session.flush()
        self.session.refresh(instance)
        return instance

    def get(self, obj_id: UUID) -> ModelT | None:
        return self.session.get(self.model, obj_id)

    def list(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[ModelT]:
        stmt = (
            select(self.model)
            .offset(offset)
            .limit(limit)
        )

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def delete(self, obj_id: UUID) -> bool:
        instance = self.get(obj_id)

        if instance is None:
            return False

        self.session.delete(instance)
        self.session.flush()

        return True