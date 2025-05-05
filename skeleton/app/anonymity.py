# Decorator for visible student to be used when student.anonymous == False
# Note that students now have a display_attributes function, which returns a dictionary to access all their variables;
# Every time we need to access data for the student, we should use this instead of just writing student.username etc, as
# It allows for anonymity to be maintained. But this can be edited in later, after the basics have been established
class VisibleStudent:
    def __init__(self, student):
        self.student = student

    def display_attributes(self):
        return {
            "uid": self.student.uid,
            "name": self.student.name,
            "username": self.student.username,
            "role": self.student.role,
            "university_email": self.student.university_email,
            "student_id": self.student.student_id,
            "forms_completed": self.student.forms_completed,
            "anonymous": self.student.anonymous,
            "flagged": self.student.flagged,
            "best_category": self.student.best_category,
            "worst_category": self.student.worst_category,
        }

    def __repr__(self):
        return (f'Student(uid={self.student.uid}, name={self.student.name}, university_email={self.student.university_email}'
                f', pwh=...{self.student.password_hash[-5:]}, student_id={self.student.student_id}, '
                f'anonymous={self.student.anonymous}, best_category={self.student.best_category},'
                f'worst_category={self.student.worst_category}, flagged={self.student.flagged}, '
                f'forms_completed={self.student.forms_completed})')
