from datetime import datetime
from app import db
from app.models import Student


class FormManagement():
    """
    This class is used to release the forms, keep track of how long has elapsed since the forms were released, and
    obtain a list of students who are behind on filling out their forms.
    """
    release_date = None
    timeframe = 30
    released = False
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FormManagement, cls).__new__(cls)
        return cls.instance
    def set_release_date(self):
        """
        :return: the date and time that the release_forms button was clicked by the staff member
        rtype: datetime
        """
        self.release_date = datetime.now()
        self.released= True
    def calculate_seconds(self):
        """
        :return: The number of seconds since the form was released
        """
        try:
            seconds = (datetime.now() - self.release_date).seconds
            return seconds
        except TypeError:
            return None
    def late_students(self):
        """
        :return: list of student objects who are behind on filling out their forms
        :rtype: int
        """
        seconds = self.calculate_seconds()
        if seconds:
            q = db.select(Student).where(Student.forms_completed < seconds/self.timeframe -1)
            student_tuples = db.session.execute(q).all()
            students = [student for student, in student_tuples]
            return students
        else:
            return None





