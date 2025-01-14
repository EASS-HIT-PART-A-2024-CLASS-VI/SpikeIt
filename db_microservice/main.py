from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_setup import init_db, SessionLocal
import db_operations

init_db()  # Initialize the database
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Drill Endpoints
@app.post("/drills/")
def create_drill(data: dict, db: Session = Depends(get_db)):
    return db_operations.create_drill(db, data)

@app.get("/drills/")
def get_drills(db: Session = Depends(get_db)):
    return db_operations.get_all_drills(db)

# Workout Endpoints
@app.post("/workouts/")
def create_workout(data: dict, db: Session = Depends(get_db)):
    return db_operations.create_workout(db, data)

@app.get("/workouts/")
def get_workouts(db: Session = Depends(get_db)):
    return db_operations.get_all_workouts(db)
