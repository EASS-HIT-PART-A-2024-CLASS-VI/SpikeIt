import sqlite3
from typing import List, Dict

DATABASE = "workouts.db"

def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS drill (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    duration INTEGER,
                    equipment TEXT,
                    type TEXT,
                    explanation TEXT,
                    workout_id INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS workout (
                    workout_id INTEGER PRIMARY KEY)''')
    conn.commit()
    conn.close()

def add_workout(workout_id: int, drills: List[Dict]):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO workout (workout_id) VALUES (?)", (workout_id,))
    for drill in drills:
        c.execute('''INSERT INTO drill (id, name, duration, equipment, type, explanation, workout_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                  (drill['id'], drill['name'], drill['duration'], drill['equipment'], drill['type'], 
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
    c.execute("SELECT * FROM workout")
    workouts = c.fetchall()
    conn.close()
    return [{"workout_id": workout[0]} for workout in workouts]
