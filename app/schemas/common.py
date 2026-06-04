from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class PaginationParams(BaseModel):
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1, le=1000)

    model_config = ConfigDict(from_attributes=True)


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    offset: int
    limit: int

    model_config = ConfigDict(from_attributes=True)