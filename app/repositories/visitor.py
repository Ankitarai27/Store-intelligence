from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.visitor import Visitor
from app.repositories.base import BaseRepository
from uuid import UUID

class VisitorRepository(BaseRepository[Visitor]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Visitor)

    def get_active_sessions(self, store_id: UUID) -> list[Visitor]:
        stmt = select(Visitor).where(
            Visitor.store_id == store_id,
            Visitor.session_end.is_(None),
        )

        result = self.session.execute(stmt)

        return list(result.scalars().all())