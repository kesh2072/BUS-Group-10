from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
import statistics
import re

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much

labels = ['stress', 'anxiety', 'self-esteem', 'depression', 'sleep']


# a function that scans the text input and returns an associated category
# ideally this would involve a supervised ML algorithm (scikit if we have time) but for now it will just search for key words
# TODO: this label_classifier doesn't work yet (currently ANY text input will be categorised as 'stress')
def label_classifier(x: str):
    # split x into list of words with regular expression
    # find the first occurrence of a key word and return as 'label'
    label='stress'
    return label

# weighting calculator: a function that takes in a list of Answer objects and outputs a dictionary of average weightings (in ascending order)
# example output: {'depression': 1.5, 'anxiety': 2, 'self-esteem': 3.5, 'sleep': 3.5, 'stress': 4.5}
def weighting(previous_answers:list):
    w={label:[] for label in labels}
    for a in previous_answers[0:10]:
        w[db.session.get(Question,a.qid).label]+=[int(a.content)]
    last_entry=previous_answers[10].content       #adjust weighting to add 5 points for the associated category of text input (if it exists)
    if last_entry:
        w[label_classifier(last_entry)]+=[5]
    w={i:statistics.mean(j) if len(j)!=0 else 0 for i,j in w.items()}
    return dict(sorted(w.items(), key=lambda i: i[1]))

# a function that counts the number of each type of question that was asked in previous iteration
# example output after first iteration: {'stress': 2, 'anxiety': 2, 'self-esteem': 2, 'depression': 2, 'sleep': 2}
def q_count(previous_answers:list):
    w = {label:0 for label in labels}
    for a in previous_answers[0:10]:
        w[db.session.get(Question, a.qid).label]+=1
    return w

# Question Generator: a function that takes in a Student object and outputs a list of 10+1 Question objects
def QG(s:Student):
    #the way i did the question_form() in the view function assumes the text question is last in the generated questions list.
    #(aimed at Maddie) i don't know if your algorithm puts the text question last in questions -if it doesn't then i can change
    #the question_form view function


    # answers exist in database: next iteration
    if s.answers:
        previous_answers=[a for a in s.answers if s.forms_completed==a.form_number]
        w=weighting(previous_answers)
        distribution=q_count(previous_answers)

        highest = list(w.keys())[-1]    # last element of w returns 'worst' category
        distribution[highest] += 1      # add an extra question for student's 'worst' category

        for label in list(w.keys()):    # first element of w (with a non-zero count) returns 'best' category
            if distribution[label]!=0:
                lowest=label
                break
        distribution[lowest] -= 1       # remove a question for student's 'best' category

        questions = []
        for label,count in distribution.items():        # return 10 questions based on new distribution (questions within each label are chosen in priority order)
            for i in range(count):
                questions+=[db.session.scalar(db.select(Question).where(Question.label==label, Question.priority==(i+1)))]
        questions+=[db.session.scalar(db.select(Question).where(Question.label=='personal'))]

        # (un)comment for debugging and understanding algorithm
        print('weighting of labels', w)
        print('distribution of questions: ', distribution)
        print('highest: ', highest)
        print('lowest: ', lowest)

        return questions

    # no answers exist in database: first iteration
    else:
        q = db.select(Question).where(sa.sql.or_(Question.priority == 1, Question.priority == 2))
        question_tuples = db.session.execute(q).all()
        questions = [question for question, in question_tuples]
        return questions
