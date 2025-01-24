import sqlite3
from typing import List, Dict

DATABASE = "workouts.db"

def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Create workout table (no changes needed here)
    c.execute('''CREATE TABLE IF NOT EXISTS workout (
                    workout_id INTEGER PRIMARY KEY AUTOINCREMENT)''')

    # Create drill table with id set to AUTOINCREMENT
    c.execute('''CREATE TABLE IF NOT EXISTS drill (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    duration INTEGER,
                    equipment TEXT,
                    type TEXT,
                    explanation TEXT,
                    workout_id INTEGER,
                    FOREIGN KEY(workout_id) REFERENCES workout(workout_id))''')

    conn.commit()
    conn.close()

def add_workout( drills: List[Dict]):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO workout DEFAULT VALUES")
    workout_id = c.lastrowid
    for drill in drills:
        c.execute('''INSERT INTO drill (name, duration, equipment, type, explanation, workout_id)
                    VALUES (?, ?, ?, ?, ?, ?)''', 
                  (drill['name'], drill['duration'], drill['equipment'], drill['type'], 
                   drill['explanation'], workout_id))
    conn.commit()
    conn.close()

def get_workout(workout_id: int) -> List[Dict]:
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM drill WHERE workout_id = ?", (workout_id,))
    drills = c.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in c.description], drill)) for drill in drills]

def get_all_workouts() -> List[Dict]:
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT workout_id FROM workout")
    workouts = c.fetchall()
    all_workouts = []
    for workout in workouts:
        workout_id = workout[0]
        c.execute("SELECT * FROM drill WHERE workout_id = ?", (workout_id,))
        drills = c.fetchall()
        drills_list = [dict(zip([column[0] for column in c.description], drill)) for drill in drills]
        all_workouts.append({"workout_id": workout_id, "drills": drills_list})
    conn.close()
    return all_workouts
