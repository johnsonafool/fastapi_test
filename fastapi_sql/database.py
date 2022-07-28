from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:johnsontseng@localhost/test_db",
echo=True)

Base = declarative_base()

Sessionmaker = sessionmaker(bind=engine)
