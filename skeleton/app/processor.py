from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
from app import app
from flask_login import current_user

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much
# Question Generator: a function that takes in a Student object and outputs a list of 10+1 Question objects (hopefully)

def QG(s):

    labels=['stress','anxiety','self-esteem','depression','sleep']

    # answers exist in database: next iteration
    if current_user:
        if s.answers:
            # return suitable list of Question objects
            questions=[]
            return questions

    # no answers exist in database: first iteration
    else:
        # return suitable list of Question objects
        q = db.select(Question).where(sa.sql.or_(Question.priority == 1, Question.priority == 2))
        question_tuples = db.session.execute(q).all()
        questions = [question for question, in question_tuples]
        return questions




