from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

# Environment variable for the database service URL
DB_SERVICE_URL = os.getenv("DB_SERVICE_URL", "http://db_service:5001")

# Drill Endpoints
@app.get("/drills/")
def get_all_drills():
    response = requests.get(f"{DB_SERVICE_URL}/drills/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/drills/")
def create_drill(data: dict):
    response = requests.post(f"{DB_SERVICE_URL}/drills/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Workout Endpoints
@app.get("/workouts/")
def get_all_workouts():
    response = requests.get(f"{DB_SERVICE_URL}/workouts/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/workouts/")
def create_workout(data: dict):
    response = requests.post(f"{DB_SERVICE_URL}/workouts/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
