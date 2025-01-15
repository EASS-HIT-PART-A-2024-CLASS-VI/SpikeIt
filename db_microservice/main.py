from fastapi import FastAPI, HTTPException
from db_operations import add_workout, get_workout, get_all_workouts
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Drill(BaseModel):
    id: int
    name: str
    duration: int
    equipment: str
    type: str
    explanation: str
    workout_id: int

class Workout(BaseModel):
    workout_id: int
    drills: List[Drill]

@app.post("/new_workout")
async def new_workout(workout: Workout):
    try:
        add_workout(workout.workout_id, [drill.dict() for drill in workout.drills])
        return {"message": "Workout created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/show_workout/{workout_id}")
async def show_workout(workout_id: int):
    drills = get_workout(workout_id)
    if not drills:
        raise HTTPException(status_code=404, detail="Workout not found")
    return drills

@app.get("/show_all_workouts")
async def show_all_workouts():
    return get_all_workouts()
