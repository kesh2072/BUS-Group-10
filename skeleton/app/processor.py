from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
from flask_login import current_user

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much
# Question Generator: a function that takes in a Student object and outputs a list of 10+1 Question objects (hopefully)

def QG(s):

    labels=['stress','anxiety','self-esteem','depression','sleep']

    # answers exist in database: next iteration
    #the way i did the question_form() in the view function assumes the text question is last in the generated questions list.
    #(aimed at Maddie) i don't know if your algorithm puts the text question last in questions -if it doesn't then i can change
    #the question_form view function

    if s:
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
