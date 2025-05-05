from app import db
from app.models import User, Student, Question, Answer
import datetime


def reset_db():

    # Haven't added any answers, and all students have currently filled out zero forms
    # Questions have labels stress, anxiety, self-esteem, depression and sleep. There is also a label 'personal' for the
    # written response at the end of the form. I've currently only got one of this type of question, but feel free to
    # add more. I've proof read the questions as they are AI generated, but they seem fine.

    db.drop_all()
    db.create_all()

    users = [
        {
            "name": "alice",
            "username": "alice",
            "role": "Admin",
            "university_email": "alice@a.com"
        },
        {
            "name": "bob",
            "username": "bob",
            "role": "Admin",
            "university_email": "bob@b.com"
        },
        {
            "name": "carol",
            "username": "carol",
            "role": "Admin",
            "university_email": "carol@c.com"
        },
        {
            "name": "dave",
            "username": "dave",
            "role": "Admin",
            "university_email": "dave@d.com"
        },
        {
            "name": "eve",
            "username": "eve",
            "role": "Admin",
            "university_email": "eve@e.com"
        },
        {
            "name": "frank",
            "username": "frank",
            "role": "Staff",
            "university_email": "frank@f.com"
        },
        {
            "name": "grace",
            "username": "grace",
            "role": "Staff",
            "university_email": "grace@g.com"
        },
        {
            "name": "heidi",
            "username": "heidi",
            "role": "Staff",
            "university_email": "heidi@h.com"
        },
        {
            "name": "ivan",
            "username": "ivan",
            "role": "Staff",
            "university_email": "ivan@i.com"
        },
        {
            "name": "judy",
            "username": "judy",
            "role": "Staff",
            "university_email": "judy@j.com"
        }
    ]

    students = [
        {
            "name": "karen",
            "username": "karen",
            "role": "Student",
            "university_email": "karen@k.com",
            "student_id": "10293847",
            "forms_completed": 2,
            "anonymous": False,
        },
        {
            "name": "leo",
            "username": "leo",
            "role": "Student",
            "university_email": "leo@l.com",
            "student_id": "29384756",
            "forms_completed": 1,
            "anonymous": True
        },
        {
            "name": "mona",
            "username": "mona",
            "role": "Student",
            "university_email": "mona@m.com",
            "student_id": "38475692",
            "forms_completed": 1,
            "anonymous": False
        },
        {
            "name": "nate",
            "username": "nate",
            "role": "Student",
            "university_email": "nate@n.com",
            "student_id": "47586920",
            "forms_completed": 1,
            "anonymous": True
        },
        {
            "name": "olga",
            "username": "olga",
            "role": "Student",
            "university_email": "olga@o.com",
            "student_id": "58392047",
            "forms_completed": 1,
            "anonymous": False
        },
        {
            "name": "paul",
            "username": "paul",
            "role": "Student",
            "university_email": "paul@p.com",
            "student_id": "69284751",
            "forms_completed": 1,
            "anonymous": True
        },
        {
            "name": "quinn",
            "username": "quinn",
            "role": "Student",
            "university_email": "quinn@q.com",
            "student_id": "73829104",
            "forms_completed": 1,
            "anonymous": False
        },
        {
            "name": "ruth",
            "username": "ruth",
            "role": "Student",
            "university_email": "ruth@r.com",
            "student_id": "84930216",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "sam",
            "username": "sam",
            "role": "Student",
            "university_email": "sam@s.com",
            "student_id": "92837465",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "tina",
            "username": "tina",
            "role": "Student",
            "university_email": "tina@t.com",
            "student_id": "13579246",
            "forms_completed": 0,
            "anonymous": True
        }
    ]

    questions = [
        {"text": "How stressed do you get about university deadlines?", "type": "Likert", "priority": 1, "label": "stress"},
        {"text": "How often do you procrastinate due to stress?", "type": "Likert", "priority": 2, "label": "stress"},
        {"text": "How well do you manage time when you're stressed?", "type": "Likert", "priority": 3, "label": "stress"},
        {"text": "How frequently do you feel emotionally exhausted?", "type": "Likert", "priority": 4, "label": "stress"},
        {"text": "How much does academic pressure affect your wellbeing?", "type": "Likert", "priority": 5, "label": "stress"},
        {"text": "How often do you avoid responsibilities due to stress?", "type": "Likert", "priority": 6, "label": "stress"},
        {"text": "How often do you cancel plans due to mental fatigue?", "type": "Likert", "priority": 7, "label": "stress"},
        {"text": "How often do you feel overwhelmed by expectations?", "type": "Likert", "priority": 8, "label": "stress"},
        {"text": "How difficult do you find it to focus under pressure?", "type": "Likert", "priority": 9, "label": "stress"},
        {"text": "How often do you feel overwhelmed by your workload?", "type": "Likert", "priority": 10, "label": "stress"},

        {"text": "How anxious do you feel in social situations at university?", "type": "Likert", "priority": 1, "label": "anxiety"},
        {"text": "How often do you feel nervous without knowing why?", "type": "Likert", "priority": 2, "label": "anxiety"},
        {"text": "How much do you worry about future events?", "type": "Likert", "priority": 3, "label": "anxiety"},
        {"text": "How tense or 'on edge' do you feel during the day?", "type": "Likert", "priority": 4, "label": "anxiety"},
        {"text": "How often do you feel overwhelmed in crowds or busy places?", "type": "Likert", "priority": 5, "label": "anxiety"},
        {"text": "How often do you find yourself worrying late at night?", "type": "Likert", "priority": 6, "label": "anxiety"},
        {"text": "How often do you experience racing thoughts?", "type": "Likert", "priority": 7, "label": "anxiety"},
        {"text": "How often do you feel nervous before social events?", "type": "Likert", "priority": 8, "label": "anxiety"},
        {"text": "How frequently do you feel anxious without knowing why?", "type": "Likert", "priority": 9, "label": "anxiety"},
        {"text": "How often do you avoid tasks due to anxiety?", "type": "Likert", "priority": 10, "label": "anxiety"},

        {"text": "How confident do you feel in your ability to handle challenges?", "type": "Likert",
         "priority": 1, "label": "self-esteem"},
        {"text": "How confident are you in social interactions?", "type": "Likert", "priority": 2, "label": "self-esteem"},
        {"text": "How in control do you feel of your emotional wellbeing?", "type": "Likert", "priority": 3, "label": "self-esteem"},
        {"text": "How supported do you feel by friends or peers?", "type": "Likert", "priority": 4, "label": "self-esteem"},
        {"text": "How comfortable are you asking others for help?", "type": "Likert", "priority": 5, "label": "self-esteem"},
        {"text": "How often do you feel a sense of purpose in your day?", "type": "Likert", "priority": 6, "label": "self-esteem"},
        {"text": "How well do you bounce back after setbacks?", "type": "Likert", "priority": 7, "label": "self-esteem"},
        {"text": "How often do you take breaks to care for your mental health?", "type": "Likert",
         "priority": 8, "label": "self-esteem"},
        {"text": "How well do you handle criticism?", "type": "Likert", "priority": 9, "label": "self-esteem"},
        {"text": "How confident are you in your decision-making?", "type": "Likert", "priority": 10, "label": "self-esteem"},

        {"text": "How often do you feel down or hopeless?", "type": "Likert", "priority": 1, "label": "depression"},
        {"text": "How often do you experience feelings of worthlessness?", "type": "Likert", "priority": 2, "label": "depression"},
        {"text": "How often do you feel that everything is an effort?", "type": "Likert", "priority": 3, "label": "depression"},
        {"text": "How frequently do you feel unmotivated?", "type": "Likert", "priority": 4, "label": "depression"},
        {"text": "How often do you feel easily irritated?", "type": "Likert", "priority": 5, "label": "depression"},
        {"text": "How frequently do you feel sad for no clear reason?", "type": "Likert", "priority": 6, "label": "depression"},
        {"text": "How often do you feel lonely?", "type": "Likert", "priority": 7, "label": "depression"},
        {"text": "How much energy do you have throughout the day?", "type": "Likert", "priority": 8, "label": "depression"},
        {"text": "How frequently do you feel joy or satisfaction in your day?", "type": "Likert",
         "priority": 9, "label": "depression"},
        {"text": "How often do you struggle to enjoy things you used to like?", "type": "Likert", "priority": 10, "label": "depression"},


        {"text": "How well do you sleep on a typical night?", "type": "Likert", "priority": 1, "label": "sleep"},
        {"text": "How easy is it for you to fall asleep at night?", "type": "Likert", "priority": 2, "label": "sleep"},
        {"text": "How satisfied are you with the quality of your sleep?", "type": "Likert", "priority": 3, "label": "sleep"},
        {"text": "How often do you wake up feeling rested?", "type": "Likert", "priority": 4, "label": "sleep"},
        {"text": "How often do you get less than six hours of sleep?", "type": "Likert", "priority": 5, "label": "sleep"},
        {"text": "How often do you lie awake with racing thoughts?", "type": "Likert", "priority": 6, "label": "sleep"},
        {"text": "How frequently do you wake up in the middle of the night?", "type": "Likert", "priority": 7, "label": "sleep"},
        {"text": "How often do you use screens right before going to bed?", "type": "Likert", "priority": 8, "label": "sleep"},
        {"text": "How satisfied are you with your sleep routine?", "type": "Likert", "priority": 9, "label": "sleep"},
        {"text": "How often do you rely on caffeine to stay awake during the day?", "type": "Likert", "priority": 10, "label": "sleep"},

        {"text": "Please describe a recent experience that affected your mental health.", "type": "Written",
         "priority": 1, "label": "personal"}
    ]

    for u in users:
        user = User(**u)
        user.set_password("PASSWORD")
        db.session.add(user)

    for s in students:
        student = Student(**s)
        student.set_password("PASSWORD")
        db.session.add(student)

    for q in questions:
        question = Question(**q)
        db.session.add(question)

    db.session.commit()


def populate():

    answers= [
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 1, "uid": 11,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 2, "uid": 11,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 11, "uid": 11,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 12, "uid": 11,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 21, "uid": 11,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 22, "uid": 11,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 31, "uid": 11,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 32, "uid": 11,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 41, "uid": 11,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 42, "uid": 11,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 9, 0), "qid": 51, "uid": 11,
         "type": "Text Answer", "content": "I feel overwhelmed almost every week now"},

        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 11,
         "type": "Likert", "content": "5"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 11,
         "type": "Likert", "content": "5"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 11,
         "type": "Likert", "content": "1"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 11,
         "type": "Likert", "content": "2"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 11,
         "type": "Likert", "content": "1"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 11,
         "type": "Likert", "content": "3"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 11,
         "type": "Likert", "content": "2"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 11,
         "type": "Likert", "content": "4"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 11,
         "type": "Likert", "content": "5"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 11,
         "type": "Likert", "content": "3"},
        {"form_number": 2, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 11,
         "type": "Text Answer", "content": ""},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 12,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 12,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 12,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 12,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 12,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 12,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 12,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 12,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 12,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 12,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 12,
         "type": "Text Answer", "content": "Sleep is hard when stress builds up"},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 13,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 13,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 13,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 13,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 13,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 13,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 13,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 13,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 13,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 13,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 13,
         "type": "Text Answer", "content": ""},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 14,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 14,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 14,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 14,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 14,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 14,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 14,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 14,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 14,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 14,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 14,
         "type": "Text Answer", "content": "Sometimes I can't focus on anything at all"},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 15,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 15,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 15,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 15,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 15,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 15,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 15,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 15,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 15,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 15,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 15,
         "type": "Text Answer", "content": ""},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 16,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 16,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 16,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 16,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 16,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 16,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 16,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 16,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 16,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 16,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 16,
         "type": "Text Answer", "content": "Some days are more stressful than others"},

        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 1, "uid": 17,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 2, "uid": 17,
         "type": "Likert", "content": "3"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 11, "uid": 17,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 12, "uid": 17,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 21, "uid": 17,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 22, "uid": 17,
         "type": "Likert", "content": "5"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 31, "uid": 17,
         "type": "Likert", "content": "1"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 32, "uid": 17,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 41, "uid": 17,
         "type": "Likert", "content": "2"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 42, "uid": 17,
         "type": "Likert", "content": "4"},
        {"form_number": 1, "submission_date": datetime.datetime(2024, 12, 1, 10, 0), "qid": 51, "uid": 17,
         "type": "Text Answer", "content": "I occasionally feel overwhelmed with assignments"}
    ]

    for a in answers:
        answer=Answer(**a)
        db.session.add(answer)

    u=db.session.get(User,11)
    u.best_category='anxiety'
    u.worst_category='stress'

    u = db.session.get(User, 12)
    u.best_category = 'stress'
    u.worst_category = 'depression'

    u = db.session.get(User, 13)
    u.best_category = 'self-esteem'
    u.worst_category = 'stress'

    u = db.session.get(User, 14)
    u.best_category = 'depression'
    u.worst_category = 'self-esteem'

    u = db.session.get(User, 15)
    u.best_category = 'depression'
    u.worst_category = 'anxiety'

    u = db.session.get(User, 16)
    u.best_category = 'depression'
    u.worst_category = 'stress'

    u = db.session.get(User, 17)
    u.best_category = 'anxiety'
    u.worst_category = 'self-esteem'




    db.session.commit()
