from typing import Generic, TypeVar, Type, Optional
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def add(self, obj: T) -> T:
        self.session.add(obj)
        self.session.flush()
        return obj

    def get(self, obj_id) -> Optional[T]:
        return self.session.query(self.model).get(obj_id)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()