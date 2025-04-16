from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from dataclasses import dataclass

# !!!!NOTE!!!! I haven't checked any of this yet, so it might not quite work. Also I'm yet to update debug_utils to
# work alongside this, so you can't use reset_db. Soz

# User class. This might seem pretty different from SW2 because we require an inheritance relation for the different
# types of user rather than only having a role feature. I implemented a getter for uid. We can discuss how we want users
# to log in, but I've temporarily included a university email for all users, plus a password. I've decided NOT to
# implement staff and admin as separate classes, because they don't really have any extra functionalities - instead,
# they work in the same way that they did in SW2 where we just specify their role. We can of course change this later.
@dataclass
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    uid: so.Mapped[int] = so.mapped_column(primary_key=True)
    university_email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    role: so.Mapped[str] = so.mapped_column(sa.String(10), default="Student")

    # Mapper args is used for inheritance relations. It tells sqlalchemy that we may want to have a separate table when
    # a user has a different role
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role,
    }

    # This function is a getter. We need to use it because some built-in SQLalchemy functions automatically
    # search for an attribute called 'id'. Because we have multiple different id types in this database,
    # I've given them names like uid (user id) or qid (question id) like Uday did in DSADB. The getter tells SQLalchemy
    # to use 'uid' as id.
    def get_id(self):
        return self.uid

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User(uid={self.uid}, username={self.username}, email={self.email}, role={self.role}, pwh=...{self.password_hash[-5:]})'


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


# Student class. Inherits from the User class in a way which I have had to google to implement (: Essentially, the
# "polymorphic_identity" allows us to have a separate table for students, because they're quite different to other
# users. I've given them a boolean for whether they're anonymous or not, and a forms_completed attribute which is
# important for using in the answers class
class Student(User):
    __tablename__ = "students"

    uid: so.Mapped[int] = so.mapped_column(ForeignKey("users.uid"), primary_key=True)
    student_id: so.Mapped[int] = so.mapped_column(index=True)
    anonymous: so.Mapped[bool] = so.mapped_column(sa.String(8), default=True)
    forms_completed: so.Mapped[int] = so.mapped_column(default=0)

    answers: so.Mapped[list["Answer"]] = relationship(back_populates="user")

    __mapper_args__ = {
        "polymorphic_identity": "student"
    }

    def __repr__(self):
        return (f'Student(uid={self.uid}, university_email={self.university_email}, student_id={self.student_id}, '
                f'anonymous={self.anonymous}, forms_completed={self.forms_completed}, pwh=...{self.password_hash[-5:]})')


# Question class. Label refers to the mental health category the question falls under - for simplicity, each question
# should only refer to one category (eg, a question should either be 'depression' or 'stress', but not both)
class Question(db.Model):
    __tablename__ = "questions"

    qid: so.Mapped[int] = so.mapped_column(primary_key=True)
    text: so.Mapped[str] = so.mapped_column(sa.String(256))
    label: so.Mapped[str] = so.mapped_column(sa.String(32))

    def get_id(self):
        return self.qid

    def __repr__(self):
        return f"Question(qid={self.qid}, text={self.text}, category={self.label}"


# Answer class. Answers will be uniquely identified by the form number, question id and user id, because a
# question may appear multiple times for the same user. 'Content' refers to the actual answer the student gave, whether
# it be a number on the likert scale, or a text response.
class Answer(db.Model):
    __tablename__ = "Answers"

    form_number: so.Mapped[int] = so.mapped_column(ForeignKey(Student.forms_completed), primary_key=True)
    qid: so.Mapped[int] = so.mapped_column(ForeignKey(Question.qid), primary_key=True)
    uid: so.Mapped[int] = so.mapped_column(ForeignKey(User.uid), primary_key=True)
    type: so.Mapped[str] = so.mapped_column(sa.String(16), default="Likert")
    content: so.Mapped[str] = so.mapped_column(sa.String(256))

    student: so.Mapped["Student"] = relationship(back_populates="answers")

    def __repr__(self):
        return f"Answer(form_number={self.form_number}, qid={self.qid}, uid={self.uid}, type={self.type}, content={self.content}"

