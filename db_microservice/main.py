from fastapi import FastAPI, HTTPException
from db_operations import add_workout, get_workout, get_all_workouts, create_db
from pydantic import BaseModel
from typing import List, Optional

create_db()

app = FastAPI()

class Drill(BaseModel):
    id: Optional[int]=None
    name: str
    duration: int
    equipment: str
    type: str
    explanation: str

class Workout(BaseModel):
    workout_id: int
    drills: List[Drill]

@app.post("/new_workout")
async def new_workout(workout: Workout):
    try:
        # Log incoming data for debugging
        print(f"Received workout: {workout}")
        
        # Insert workout and drills into the database
        add_workout([drill.dict() for drill in workout.drills])
        return {"message": "Workout created successfully"}
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log the error
        raise HTTPException(status_code=400, detail="Failed to create workout")


@app.get("/show_workout/{workout_id}")
async def show_workout(workout_id: int):
    drills = get_workout(workout_id)
    if not drills:
        raise HTTPException(status_code=404, detail="Workout not found")
    return drills

@app.get("/show_all_workouts")
async def show_all_workouts():
    return get_all_workouts()
