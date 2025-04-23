from app.models import Student, Question, Answer
from app import db

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much
# Question Generator: a function that takes in a Student object and outputs a list of 10+1 Question objects (hopefully)

def QG(s):

    labels=['stress','anxiety','self-esteem','depression','sleep']

    # answers exist in database: next iteration
    if s.answers:
        # return suitable list of Question objects
        questions=[]
        return questions

    # no answers exist in database: first iteration
    else:
        # return suitable list of Question objects
        questions=[]
        return questions
