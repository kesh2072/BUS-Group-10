from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
import statistics

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much

labels = ['stress', 'anxiety', 'self-esteem', 'depression', 'sleep']

# weighting calculator: a function that takes in a list of Answer objects and outputs a dictionary of average weightings
# example output: {'stress': 1.5, 'anxiety': 0, 'self-esteem': 4, 'depression': 0, 'sleep': 0}
def weighting(previous_answers:list):
    w={label:[] for label in labels}
    for a in previous_answers[0:10]:
        w[db.session.get(Question,a.qid).label]+=[int(a.content)]
    w={i:statistics.mean(j) if len(j)!=0 else 0 for i,j in w.items()}
    return w

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

    # TODO: this algorithm does not process the text input yet

    # answers exist in database: next iteration
    if s.answers:
        # return suitable list of Question objects
        previous_answers=[a for a in s.answers if s.forms_completed==a.form_number]
        sorted_by_weight=dict(sorted(weighting(previous_answers).items(), key=lambda i: i[1]))
        highest=list(sorted_by_weight.keys())[-1]    # last element of sorted_by_weight returns 'worst' category
        lowest=list(sorted_by_weight.keys())[0]
        distribution=q_count(previous_answers)

        # TODO: needs adjusting for special cases (ie no more to remove)
        # TODO: hence this form page will only work for a few iterations right now before it crashes
        # add an extra question for student's 'worst' category
        # remove a question for student's 'best' category
        distribution[highest]+=1
        distribution[lowest]-=1

        questions = []
        for label,count in distribution.items():
            for i in range(count):
                questions+=[db.session.scalar(db.select(Question).where(Question.label==label, Question.priority==(i+1)))]
        questions+=[db.session.scalar(db.select(Question).where(Question.label=='personal'))]
        return questions

    # no answers exist in database: first iteration
    else:
        # return suitable list of Question objects
        q = db.select(Question).where(sa.sql.or_(Question.priority == 1, Question.priority == 2))
        question_tuples = db.session.execute(q).all()
        questions = [question for question, in question_tuples]
        return questions
