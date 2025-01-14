from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
DATABASE_URL = "sqlite:///./drills_workouts.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models
class Drill(Base):
    __tablename__ = 'drills'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)
    equipment = Column(String, nullable=False)

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    drills = Column(Text, nullable=False)  # Storing drill IDs as JSON

def init_db():
    Base.metadata.create_all(bind=engine)
