# Decorator for visible student to be used when student.anonymous == False
class VisibleStudent:
    def __init__(self, student):
        self.student = student

    def __repr__(self):
        return (f'Student(uid={self.student.uid}, name={self.student.name}, university_email={self.student.university_email}'
                f', pwh=...{self.student.password_hash[-5:]}, student_id={self.student.student_id}, '
                f'anonymous={self.student.anonymous}, forms_completed={self.student.forms_completed})')
