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
            "university_email": "karen@example.com",
            "student_id": "10293847",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "leo",
            "username": "leo",
            "role": "Student",
            "university_email": "leo@example.com",
            "student_id": "29384756",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "mona",
            "username": "mona",
            "role": "Student",
            "university_email": "mona@example.com",
            "student_id": "38475692",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "nate",
            "username": "nate",
            "role": "Student",
            "university_email": "nate@example.com",
            "student_id": "47586920",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "olga",
            "username": "olga",
            "role": "Student",
            "university_email": "olga@example.com",
            "student_id": "58392047",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "paul",
            "username": "paul",
            "role": "Student",
            "university_email": "paul@example.com",
            "student_id": "69284751",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "quinn",
            "username": "quinn",
            "role": "Student",
            "university_email": "quinn@example.com",
            "student_id": "73829104",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "ruth",
            "username": "ruth",
            "role": "Student",
            "university_email": "ruth@example.com",
            "student_id": "84930216",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "sam",
            "username": "sam",
            "role": "Student",
            "university_email": "sam@example.com",
            "student_id": "92837465",
            "forms_completed": 0,
            "anonymous": False
        },
        {
            "name": "tina",
            "username": "tina",
            "role": "Student",
            "university_email": "tina@example.com",
            "student_id": "13579246",
            "forms_completed": 0,
            "anonymous": True
        },
        {
            "name": "test user",
            "username": "test user",
            "role": "Student",
            "university_email": "testuserformreminder@outlook.com",
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
