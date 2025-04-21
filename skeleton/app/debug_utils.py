from app import db
from app.models import User, Student, Question, Answer


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
            "role": "Admin",
            "university_email": "alice@a.com"
        },
        {
            "name": "bob",
            "role": "Admin",
            "university_email": "bob@b.com"
        },
        {
            "name": "carol",
            "role": "Admin",
            "university_email": "carol@c.com"
        },
        {
            "name": "dave",
            "role": "Admin",
            "university_email": "dave@d.com"
        },
        {
            "name": "eve",
            "role": "Admin",
            "university_email": "eve@e.com"
        },
        {
            "name": "frank",
            "role": "Staff",
            "university_email": "frank@f.com"
        },
        {
            "name": "grace",
            "role": "Staff",
            "university_email": "grace@g.com"
        },
        {
            "name": "heidi",
            "role": "Staff",
            "university_email": "heidi@h.com"
        },
        {
            "name": "ivan",
            "role": "Staff",
            "university_email": "ivan@i.com"
        },
        {
            "name": "judy",
            "role": "Staff",
            "university_email": "judy@j.com"
        }
    ]

    students = [
        {
            "name": "karen",
            "role": "Student",
            "university_email": "karen@k.com",
            "student_id": "10293847",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "leo",
            "role": "Student",
            "university_email": "leo@l.com",
            "student_id": "29384756",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "mona",
            "role": "Student",
            "university_email": "mona@m.com",
            "student_id": "38475692",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "nate",
            "role": "Student",
            "university_email": "nate@n.com",
            "student_id": "47586920",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "olga",
            "role": "Student",
            "university_email": "olga@o.com",
            "student_id": "58392047",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "paul",
            "role": "Student",
            "university_email": "paul@p.com",
            "student_id": "69284751",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "quinn",
            "role": "Student",
            "university_email": "quinn@q.com",
            "student_id": "73829104",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "ruth",
            "role": "Student",
            "university_email": "ruth@r.com",
            "student_id": "84930216",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "sam",
            "role": "Student",
            "university_email": "sam@s.com",
            "student_id": "92837465",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "tina",
            "role": "Student",
            "university_email": "tina@t.com",
            "student_id": "13579246",
            "forms_completed": 0,
            "anonymous": True
        }
    ]

    questions = [
        {"text": "How stressed do you get about university deadlines?", "type": "Likert", "label": "stress"},
        {"text": "How often do you procrastinate due to stress?", "type": "Likert", "label": "stress"},
        {"text": "How well do you manage time when you're stressed?", "type": "Likert", "label": "stress"},
        {"text": "How frequently do you feel emotionally exhausted?", "type": "Likert", "label": "stress"},
        {"text": "How much does academic pressure affect your wellbeing?", "type": "Likert", "label": "stress"},
        {"text": "How often do you avoid responsibilities due to stress?", "type": "Likert", "label": "stress"},
        {"text": "How often do you cancel plans due to mental fatigue?", "type": "Likert", "label": "stress"},
        {"text": "How often do you feel overwhelmed by expectations?", "type": "Likert", "label": "stress"},
        {"text": "How difficult do you find it to focus under pressure?", "type": "Likert", "label": "stress"},
        {"text": "How often do you feel overwhelmed by your workload?", "type": "Likert", "label": "stress"},

        {"text": "How anxious do you feel in social situations at university?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you feel nervous without knowing why?", "type": "Likert", "label": "anxiety"},
        {"text": "How much do you worry about future events?", "type": "Likert", "label": "anxiety"},
        {"text": "How tense or 'on edge' do you feel during the day?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you feel overwhelmed in crowds or busy places?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you find yourself worrying late at night?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you experience racing thoughts?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you feel nervous before social events?", "type": "Likert", "label": "anxiety"},
        {"text": "How frequently do you feel anxious without knowing why?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you avoid tasks due to anxiety?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you stay up worrying?", "type": "Likert", "label": "anxiety"},
        {"text": "How often do you feel unable to relax?", "type": "Likert", "label": "anxiety"},
        {"text": "How frequently do you worry about things beyond your control?", "type": "Likert", "label": "anxiety"},

        {"text": "How confident do you feel in your ability to handle challenges?", "type": "Likert",
         "label": "self-esteem"},
        {"text": "How confident are you in social interactions?", "type": "Likert", "label": "self-esteem"},
        {"text": "How in control do you feel of your emotional wellbeing?", "type": "Likert", "label": "self-esteem"},
        {"text": "How supported do you feel by friends or peers?", "type": "Likert", "label": "self-esteem"},
        {"text": "How comfortable are you asking others for help?", "type": "Likert", "label": "self-esteem"},
        {"text": "How often do you feel a sense of purpose in your day?", "type": "Likert", "label": "self-esteem"},
        {"text": "How well do you bounce back after setbacks?", "type": "Likert", "label": "self-esteem"},
        {"text": "How often do you take breaks to care for your mental health?", "type": "Likert",
         "label": "self-esteem"},
        {"text": "How well do you handle criticism?", "type": "Likert", "label": "self-esteem"},
        {"text": "How confident are you in your decision-making?", "type": "Likert", "label": "self-esteem"},

        {"text": "How often do you feel down or hopeless?", "type": "Likert", "label": "depression"},
        {"text": "How often do you experience feelings of worthlessness?", "type": "Likert", "label": "depression"},
        {"text": "How often do you feel that everything is an effort?", "type": "Likert", "label": "depression"},
        {"text": "How frequently do you feel unmotivated?", "type": "Likert", "label": "depression"},
        {"text": "How often do you feel easily irritated?", "type": "Likert", "label": "depression"},
        {"text": "How frequently do you feel sad for no clear reason?", "type": "Likert", "label": "depression"},
        {"text": "How often do you feel lonely?", "type": "Likert", "label": "depression"},
        {"text": "How much energy do you have throughout the day?", "type": "Likert", "label": "depression"},
        {"text": "How frequently do you feel joy or satisfaction in your day?", "type": "Likert",
         "label": "depression"},

        {"text": "How well do you sleep on a typical night?", "type": "Likert", "label": "sleep"},
        {"text": "How easy is it for you to fall asleep at night?", "type": "Likert", "label": "sleep"},
        {"text": "How satisfied are you with the quality of your sleep?", "type": "Likert", "label": "sleep"},
        {"text": "How often do you wake up feeling rested?", "type": "Likert", "label": "sleep"},
        {"text": "How often do you get less than six hours of sleep?", "type": "Likert", "label": "sleep"},
        {"text": "How often do you lie awake with racing thoughts?", "type": "Likert", "label": "sleep"},

        {"text": "Please describe a recent experience that affected your mental health.", "type": "Written",
         "label": "personal"}
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
