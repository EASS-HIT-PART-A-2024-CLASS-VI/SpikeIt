from sqlalchemy.orm import Session
from db_setup import Drill, Workout

# Drill Operations
def create_drill(db: Session, data: dict):
    drill = Drill(**data)
    db.add(drill)
    db.commit()
    db.refresh(drill)
    return drill

def get_all_drills(db: Session):
    return db.query(Drill).all()

# Workout Operations
def create_workout(db: Session, data: dict):
    workout = Workout(**data)
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

def get_all_workouts(db: Session):
    return db.query(Workout).all()
