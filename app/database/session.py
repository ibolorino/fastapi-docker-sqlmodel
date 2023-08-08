from sqlmodel import Session, create_engine

from app.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URI, echo=True)

local_session = Session(engine)
