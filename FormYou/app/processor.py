from app.models import Student, Question, Answer
from app import db
import sqlalchemy as sa
import statistics
import re


class MLQuestionProcessingManager:
    """
    This class is responsible for processing all form responses.
    """
    current_s = None

    labels = ['stress', 'anxiety', 'self-esteem', 'depression', 'sleep']

    def __new__(cls):
        """
        There will only be one instance of this class at any time throughout execution.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(MLQuestionProcessingManager, cls).__new__(cls)
        return cls.instance

    def label_classifier(self,x: str):
        """
        This processes the text response in a student's form submission.
        It will return the label of the category for which the student enters the most keywords, or None if no keywords
        are present in the text response. In the case where there are the same number of occurrences of words for two
        (or more) categories, the function returns the key that occurs first in keyword_count dictionary.

        On top of this, if the word 'danger' is found in the text, the student's 'flagged' attribute is set to True

        :param x: student response in text field
        :type x: str
        :return: the label associated with the first key word in text response, or None if one cannot be found
        :rtype: str
        """

        keyword_dict = {'stress': ['stress', 'stressed', 'overwhelmed', 'exams', 'deadlines', 'pressure'],
                        'anxiety': ['anxious', 'anxiety', 'worried', 'worry', 'panic', 'avoid'],
                        'self-esteem': ['failure', 'confidence', 'confident', 'worthless',
                                        'selfesteem', 'self'],
                        'depression': ['depressed', 'depression', 'sad', 'hopeless', 'cried', 'numb'],
                        'sleep': ['slept', 'sleep', 'insomnia', 'tired', 'awake', 'night']}

        keyword_count = {'stress': 0, 'anxiety': 0, 'self-esteem': 0, 'depression': 0, 'sleep': 0}

        text = re.sub(r'[^\w\s]', '', x)
        # note this turns self-esteem into selfesteem which is why 'selfesteem' is in the keyword_dict
        text_list = text.split(' ')
        
        if 'danger' in text_list:
            self.current_s.flagged = True
            db.session.commit()
            text_list = [word for word in text_list if word != 'danger']

        for key, value in keyword_dict.items():
            for word in text_list:
                if word.lower() in value:
                    keyword_count[key] += 1
        label = max(keyword_count, key=keyword_count.get)
        
        if keyword_count[label] == 0:
            return None
        else:
            return label

    def weighting(self, previous_answers: list):
        """
        calculates weightings of each category given a student's last set of form responses. If the text response
        can be classified, its weight is equivalent to that of a student choosing '5' on a question of its category

        :param previous_answers: a list of Answer objects from latest form submission
        :type previous_answers: list
        :return: dictionary of average weightings in ascending order eg: {'depression': 1.5, 'anxiety': 2, 'self-esteem': 3.5, 'sleep': 3.5, 'stress': 4.5}
        :rtype: dict
        """

        w = {label: [] for label in self.labels}
        for a in previous_answers[0:10]:
            w[db.session.get(Question, a.qid).label] += [int(a.content)]
        last_entry = previous_answers[10].content       # adjust weighting to add 5 points for the associated category of text input (if it exists)
        if last_entry:
            if self.label_classifier(last_entry):
                w[self.label_classifier(last_entry)] += [5]
        w = {i: statistics.mean(j) if len(j) != 0 else 0 for i, j in w.items()}
        return dict(sorted(w.items(), key=lambda i: i[1]))

    def q_count(self, previous_answers: list):
        """
        counts the number of each category of question that was asked in previous form

        :param previous_answers: a list of Answer objects from latest form submission
        :type previous_answers: list
        :return: dictionary of the number of each category of question eg: {'stress': 2, 'anxiety': 2, 'self-esteem': 2, 'depression': 2, 'sleep': 2}
        :rtype: dict
        """

        w = {label: 0 for label in self.labels}
        for a in previous_answers[0:10]:
            w[db.session.get(Question, a.qid).label] += 1
        return w

    def worst_best(self, s: Student):
        """
        calculates the student's best and worst categories given their latest form responses.

        :param s: the current Student object
        :type s: Student
        :return: a tuple for their (worst,best) categories or (None,None) if no forms have been filled yet
        :rtype:tuple
        """

        if s.answers:
            previous_answers = [a for a in s.answers if s.forms_completed == a.form_number]
            w = self.weighting(previous_answers)
            distribution = self.q_count(previous_answers)
            worst = list(w.keys())[-1]          # last element of w returns 'worst' category
            for label in list(w.keys()):        # first element of w (with a non-zero count) returns 'best' category
                if distribution[label] != 0:
                    best = label
                    break
            return worst, best
        else:
            return None,None

    def question_generator(self, s: Student):
        """
        Question Generator: chooses the next iteration of 10 questions for the student + the text field
        One question is added for the worst category and one is removed from the best category

        :param s: the current Student object
        :type s: Student
        :return: list of 11 Question objects
        :rtype: list
        """

        self.current_s = s
        
        # answers exist in database: next iteration
        if s.answers:
            previous_answers = [a for a in s.answers if s.forms_completed == a.form_number]
            worst, best = self.worst_best(s)
            distribution = self.q_count(previous_answers)

            distribution[worst] += 1      # add an extra question for student's 'worst' category
            distribution[best] -= 1       # remove a question for student's 'best' category

            questions = []
            for label,count in distribution.items():        # return 10 questions based on new distribution (questions within each label are chosen in priority order)
                for i in range(count):
                    questions += [db.session.scalar(db.select(Question).where(Question.label == label, Question.priority == (i+1)))]
            questions += [db.session.scalar(db.select(Question).where(Question.label == 'personal'))]

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
