from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from typing import List, Optional

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
    drills: list[Drill]

@app.get("/")
async def root():
    return {"message": "Welcome to SpikeIt!"}

@app.post("/new_workout/")
async def new_workout(workout: Workout):
    # Prepare the data and send it to the DB microservice
    async with httpx.AsyncClient() as client:
        payload = {
            "workout_id": workout.workout_id,
            "drills": [drill.dict() for drill in workout.drills]  # Ensure this is properly formatted
        }
        response = await client.post("http://db_microservice:8001/new_workout", json=payload)
        if response.status_code == 200:
            return {"message": "Workout created successfully"}
        raise HTTPException(status_code=400, detail="Failed to create workout")


@app.get("/show_workout/{workout_id}")
async def show_workout(workout_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://db_microservice:8001/show_workout/{workout_id}")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=404, detail="Workout not found")

@app.get("/show_all_workouts/")
async def show_all_workouts():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://db_microservice:8001/show_all_workouts")
        return response.json()