from typing import Optional, Annotated

from sqlalchemy import func
from sqlmodel import TIMESTAMP, Column, Field
from sqlalchemy.orm import declarative_mixin
from datetime import datetime, timezone


def utcnow():
    return datetime.now(timezone.utc)


@declarative_mixin
class HasSequenceID:
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)


@declarative_mixin
class HasCreatedAt:
    created_at: Annotated[datetime, Field(
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": utcnow,
            "nullable": False,
        },
        sa_type=TIMESTAMP(timezone=True)
    )]


@declarative_mixin
class HasUpdatedAt:
    updated_at: Annotated[datetime, Field(
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": utcnow,
            "nullable": False,
        },
        sa_type=TIMESTAMP(timezone=True)
    )]