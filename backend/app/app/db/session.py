from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(url=settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
