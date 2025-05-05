from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
import statistics
import re

# This makes the app more modular, which helps with neater code and testing. Also, it means we don't mess around with views.py too much

class MLQuestionProcessingManager:

    labels = ['stress', 'anxiety', 'self-esteem', 'depression', 'sleep']

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MLQuestionProcessingManager, cls).__new__(cls)
        return cls.instance

    # a function that scans the text input and returns an associated category
    # ideally this would involve a supervised ML algorithm (scikit if we have time) but for now it will just search for key words
    # TODO: this label_classifier doesn't work yet (currently ANY text input will be categorised as 'stress')
    # TODO: for simplicity's sake, ANY text input must belong to a category
    def label_classifier(self,x: str):


        keyword_dict = {'stress': ['stress', 'stressed', 'overwhelmed', 'exams', 'deadlines', 'pressure'],
                        'anxiety': ['anxious', 'anxiety', 'worried', 'worry', 'panic', 'avoid'],
                        'self-esteem': ['failure', 'confidence', 'confident', 'worthless',
                                        'selfesteem', 'useless'],
                        'depression': ['depressed', 'depression', 'sad', 'hopeless', 'cried', 'numb'],
                        'sleep': ['slept', 'sleep', 'insomnia', 'tired', 'awake', 'night']}

        keyword_count = {'stress': 0, 'anxiety': 0, 'self-esteem': 0, 'depression': 0, 'sleep': 0}

        text = re.sub(r'[^\w\s]', '', x)   #note this turns self-esteem into selfesteem which is why 'selfesteem'
        #is in the keyword_dict
        text_list = text.split(' ')

        for key, value in keyword_dict.items():
            for word in text_list:
                if word.lower() in value:
                    keyword_count[key] += 1
        label = max(keyword_count, key=keyword_count.get)
        if keyword_count[label] == 0:
            return None
        else:
            return label
    # weighting calculator: a function that takes in a list of Answer objects and outputs a dictionary of average weightings (in ascending order)
    # example output: {'depression': 1.5, 'anxiety': 2, 'self-esteem': 3.5, 'sleep': 3.5, 'stress': 4.5}
    def weighting(self,previous_answers:list):
        w={label:[] for label in self.labels}
        for a in previous_answers[0:10]:
            w[db.session.get(Question,a.qid).label]+=[int(a.content)]
        last_entry=previous_answers[10].content       #adjust weighting to add 5 points for the associated category of text input (if it exists)
        if last_entry:
            if self.label_classifier(last_entry):
                w[self.label_classifier(last_entry)]+=[5]
        w={i:statistics.mean(j) if len(j)!=0 else 0 for i,j in w.items()}
        return dict(sorted(w.items(), key=lambda i: i[1]))

    # a function that counts the number of each type of question that was asked in previous iteration
    # example output after first iteration: {'stress': 2, 'anxiety': 2, 'self-esteem': 2, 'depression': 2, 'sleep': 2}
    def q_count(self,previous_answers:list):
        w = {label:0 for label in self.labels}
        for a in previous_answers[0:10]:
            w[db.session.get(Question, a.qid).label]+=1
        return w

    #a function that returns the student's best and worst categories
    def worst_best(self,s:Student):
        if s.answers:
            previous_answers=[a for a in s.answers if s.forms_completed==a.form_number]
            w = self.weighting(previous_answers)
            distribution = self.q_count(previous_answers)
            worst = list(w.keys())[-1]        # last element of w returns 'worst' category
            for label in list(w.keys()):        # first element of w (with a non-zero count) returns 'best' category
                if distribution[label] != 0:
                    best = label
                    break
            return worst,best
        else:
            return None,None

    # Question Generator: a function that takes in a Student object and outputs a list of 10+1 Question objects
    def QG(self,s:Student):
        #the way i did the question_form() in the view function assumes the text question is last in the generated questions list.
        #(aimed at Maddie) i don't know if your algorithm puts the text question last in questions -if it doesn't then i can change
        #the question_form view function

        # answers exist in database: next iteration
        if s.answers:
            previous_answers=[a for a in s.answers if s.forms_completed==a.form_number]
            worst,best = self.worst_best(s)
            distribution=self.q_count(previous_answers)

            distribution[worst] += 1      # add an extra question for student's 'worst' category
            distribution[best] -= 1       # remove a question for student's 'best' category

            questions = []
            for label,count in distribution.items():        # return 10 questions based on new distribution (questions within each label are chosen in priority order)
                for i in range(count):
                    questions+=[db.session.scalar(db.select(Question).where(Question.label==label, Question.priority==(i+1)))]
            questions+=[db.session.scalar(db.select(Question).where(Question.label=='personal'))]

            # (un)comment for debugging and understanding algorithm
            print('weighting of labels', self.weighting(previous_answers))
            print('distribution of questions: ', distribution)
            print('worst: ', worst)
            print('best: ', best)


            return questions

        # no answers exist in database: first iteration
        else:
            q = db.select(Question).where(sa.sql.or_(Question.priority == 1, Question.priority == 2))
            question_tuples = db.session.execute(q).all()
            questions = [question for question, in question_tuples]
            return questions
