from sqlmodel import Field, SQLModel, Column, Integer
from app.lib.mixins import HasSequenceID, HasCreatedAt, HasUpdatedAt


class User(SQLModel, HasSequenceID, HasCreatedAt, HasUpdatedAt, table=True):
    tg_id: int = Field(sa_column=Column(Integer, index=True, unique=True, nullable=False))
