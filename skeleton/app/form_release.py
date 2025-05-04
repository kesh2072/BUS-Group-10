from datetime import datetime
from app import db
from app.models import Student


class FormManagement():
    release_date = None
    timeframe = 10
    released = False
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FormManagement, cls).__new__(cls)
        return cls.instance
    def set_release_date(self):
        self.release_date = datetime.now()
        self.released= True
    def calculate_seconds(self):
        try:
            seconds = (datetime.now() - self.release_date).seconds
            return seconds
        except TypeError:
            return None
    def late_students(self):
        #gets list of student objects for students who haven't filled out 1 form after 30 seconds,
        # 2 forms after 60 seconds, 3 forms after 90 seconds etc.
        #30 seconds used here represents 2 weeks

        seconds = self.calculate_seconds()
        if seconds:
            q = db.select(Student).where(Student.forms_completed < seconds/self.timeframe -1)
            student_tuples = db.session.execute(q).all()
            students = [student for student, in student_tuples]
            return students
        else:
            return None





