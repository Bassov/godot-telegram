from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

from app.config import env

engine = create_engine(str(env.postgres.dsn))

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
