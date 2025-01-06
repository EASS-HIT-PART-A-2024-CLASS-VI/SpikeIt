class Drill:
    id=0
    def __init__(self, name, subject, duration, note, type):
        self._id=id=1
        id=id+1
        self._name = name
        self._subject = subject
        self._duration = duration
        self._note = note
        self._type = type  


    # Getter methods
    def get_id(self):
        return self._id
    
    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_subject(self):
        return self._subject

    def get_duration(self):
        return self._duration

    def get_note(self):
        return self._note

    # Setter methods
    def set_type(self, drill_type):
        self._type = drill_type
    def set_name(self, name):
        self._name = name

    def set_subject(self, subject):
        self._subject = subject

    def set_duration(self, duration):
        self._duration = duration

    def set_note(self, note):
        self._note = note
    
    def to_str(self):
        s="Drill: {self._name} - {self._subject} - {self._duration}  - {self._type} \n {self._note}"
