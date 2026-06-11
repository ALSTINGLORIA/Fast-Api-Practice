from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Database_URL = "postgresql+psycopg2://postgres:password@localhost:5432/mission_control"

engine = create_engine(Database_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
