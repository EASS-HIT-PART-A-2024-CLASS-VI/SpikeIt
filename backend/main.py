from fastapi import FastAPI, HTTPException
import workout, drill

app = FastAPI()
workouts = []

@app.get("/")
def read_root():
    return {"message": "welcome to SpikeIt!"}

@app.get("/workouts")
def read_workouts():
    for w in workouts:
        print(w.to_str())

@app.get("/workouts/{workout_id}")
def read_workout(workout_id: int):
    try:
        print(workouts[workout_id].to_str())
    except IndexError:
        raise HTTPException(status_code=404, detail="Workout not found")

@app.post("/addWorkout")
def add_workout(name: str):
    new_workout = workout.Workout(name)
    workouts.append(new_workout)
    return new_workout

@app.post("/addWorkout/addDrill")
def add_drill(workout: workout, name: str, subject: str, duration: int, note: str, type : str):
    new_drill = drill.Drill(name, subject, duration, note, type)
    workout.add_drill(new_drill)
    return new_drill




