import drill
from datetime import date
from datetime import datetime
class Workout:
    id=0
    def __init__(self, name):
        self._id=id+1
        self._name = name
        self._drills = []
        self._workout_date = datetime.now()
        id+=1

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def add_drill(self, drill):
        self._drills.append(drill)

    def get_workout_date(self):
        return self._workout_date
    
    def to_str(self):
        s="Workout: {self._name} on {self._workout_date} \n"
        for d in self._drills:
            s+=d.to_str()+"\n"
            return s
        

