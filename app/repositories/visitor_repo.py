from sqlalchemy.orm import Session
from app.models.visitor import Visitor
from app.repositories.base import BaseRepository


class VisitorRepository(BaseRepository[Visitor]):
    def __init__(self, session: Session):
        super().__init__(Visitor, session)

    def get_active_session(self, visitor_id):
        return (
            self.session.query(Visitor)
            .filter(
                Visitor.id == visitor_id,
                Visitor.session_end.is_(None),
            )
            .first()
        )