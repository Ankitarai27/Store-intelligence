from datetime import datetime, timedelta
from app.models.visitor import Visitor


class VisitorService:
    SESSION_TIMEOUT_MINUTES = 30

    def __init__(self, visitor_repo):
        self.visitor_repo = visitor_repo

    def get_or_create_session(self, visitor_id, store_id, timestamp: datetime):
        visitor = self.visitor_repo.get(visitor_id)

        if not visitor:
            visitor = Visitor(
                id=visitor_id,
                store_id=store_id,
                session_start=timestamp,
                is_staff=False,
                is_converted=False,
            )
            self.visitor_repo.add(visitor)
            return visitor

        # session timeout logic
        if visitor.session_end:
            visitor.session_start = timestamp
            visitor.session_end = None

        return visitor

    def close_session(self, visitor: Visitor, timestamp: datetime):
        visitor.session_end = timestamp