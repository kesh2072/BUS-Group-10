from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from dataclasses import dataclass
import datetime


# User classes implement inheritance relations
@dataclass
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    uid: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(32), index=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), index=True)
    university_email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    role: so.Mapped[str] = so.mapped_column(sa.String(10), default="Student")

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role,
    }

    def get_id(self):
        return self.uid

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return (f'User(uid={self.uid}, username={self.username}, university_email={self.university_email}, pwh=...{self.password_hash[-5:]},'
                f' role={self.role})')


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


class Student(User):
    __tablename__ = "students"

    uid: so.Mapped[int] = so.mapped_column(ForeignKey("users.uid"), primary_key=True)
    student_id: so.Mapped[int] = so.mapped_column(index=True)
    flagged: so.Mapped[bool] = so.mapped_column(sa.Boolean(), default=False)
    anonymous: so.Mapped[bool] = so.mapped_column(sa.Boolean(), default=True)
    forms_completed: so.Mapped[int] = so.mapped_column(default=0)
    best_category: so.Mapped[Optional[str]] = so.mapped_column(default=None)
    worst_category: so.Mapped[Optional[str]] = so.mapped_column(default=None)

    answers: so.Mapped[list["Answer"]] = relationship(back_populates="student", cascade="all, delete-orphan")

    __mapper_args__ = {
        "polymorphic_identity": "Student"
    }

    def display_attributes(self):
        return {
            "uid": self.uid,
            "name": "----",
            "username": "----",
            "role": self.role,
            "university_email": "----",
            "student_id": "----",
            "forms_completed": self.forms_completed,
            "anonymous": self.anonymous,
            "flagged": self.flagged,
            "best_category": self.best_category,
            "worst_category": self.worst_category,
        }

    def __repr__(self):
        return (f'Student(uid={self.uid}, name={self.name}, university_email={self.university_email}, '
                f'pwh=...{self.password_hash[-5:]}, student_id={self.student_id}, anonymous={self.anonymous}, '
                f'best_category={self.best_category}, worst_category={self.worst_category}, flagged={self.flagged} '
                f'forms_completed={self.forms_completed})')


# Decorator for visible student to be used when student.anonymous == False
# Changes the display_attributes method of the student class (note that attributes should always be accessed via
# this function)
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


class Admin(User):
    __mapper_args__ = {
        "polymorphic_identity": "Admin"
    }


class Staff(User):
    __mapper_args__ = {
        "polymorphic_identity": "Staff"
    }


# Question class. Each question relates to one mental health category
class Question(db.Model):
    __tablename__ = "questions"

    __table_args__ = (
        sa.UniqueConstraint("label", "priority"),
    )

    qid: so.Mapped[int] = so.mapped_column(primary_key=True)
    text: so.Mapped[str] = so.mapped_column(sa.String(256))
    type: so.Mapped[str] = so.mapped_column(sa.String(16), default="Likert")
    priority: so.Mapped[int] = so.mapped_column()
    label: so.Mapped[str] = so.mapped_column(sa.String(32))

    answers: so.Mapped["Answer"] = relationship(back_populates="question")

    def get_id(self):
        return self.qid

    def __repr__(self):
        return (f"Question(qid={self.qid}, text={self.text}, type={self.type}, priority={self.priority}, "
                f"label={self.label}")


# Answer class, created whenever a student fills out a form
class Answer(db.Model):
    __tablename__ = "Answers"

    form_number: so.Mapped[int] = so.mapped_column(primary_key=True)
    submission_date: so.Mapped[datetime.datetime] = so.mapped_column(DateTime(timezone=True), default=None)
    qid: so.Mapped[int] = so.mapped_column(ForeignKey(Question.qid), primary_key=True)
    uid: so.Mapped[int] = so.mapped_column(ForeignKey(Student.uid), primary_key=True)
    type: so.Mapped[str] = so.mapped_column(sa.String(16), default="Likert")
    content: so.Mapped[str] = so.mapped_column(sa.String(256))

    student: so.Mapped["Student"] = relationship(back_populates="answers")
    question: so.Mapped["Question"] = relationship(back_populates="answers")

    def __repr__(self):
        return (f"Answer(form_number={self.form_number}, qid={self.qid}, uid={self.uid}, type={self.type}, "
                f"content={self.content})")


class Resource(db.Model):
    __tablename__ = "resources"

    rid: so.Mapped[int] = so.mapped_column(primary_key=True)
    type: so.Mapped[str] = so.mapped_column(sa.String())
    title: so.Mapped[str] = so.mapped_column(sa.String())
    description: so.Mapped[str] = so.mapped_column(sa.String())
    logo: so.Mapped[str] = so.mapped_column(sa.String())
    url: so.Mapped[str] = so.mapped_column(sa.String())
    is_recommended: so.Mapped[bool] = so.mapped_column(db.Boolean, default=False)

    def __repr__(self):
        return f"rid={self.rid}, title={self.title}, description={self.description}, logo={self.logo}, url={self.url}"
