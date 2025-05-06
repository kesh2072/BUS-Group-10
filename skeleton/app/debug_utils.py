from app import db
from app.models import User, Student, Question, Answer, Resource
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
            "university_email": "karen@example.com",
            "student_id": "10293847",
            "forms_completed": 0,
            "anonymous": False,
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

    resources = [
                {'type': 'stress', 'title': 'Student stress', 'description': 'Tips on student stress: ways to detect symptoms and handle it better', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/mental-health/children-and-young-adults/help-for-teenagers-young-adults-and-students/student-stress-self-help-tips/"},
                {'type': 'stress', 'title': '5 ways to manage student stress', 'description': 'Tips on handling your stress better as a student', 'logo': 'logos/prospects.png', 'url': "https://www.prospects.ac.uk/applying-for-university/university-life/5-ways-to-manage-student-stress#:~:text=If%20possible%20leave%20your%20stresses,the%20triggers%20of%20your%20stressors."},
                {'type': 'stress', 'title': 'Dealing with stress', 'description': 'Details on what causes stress and how we can better deal with it', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/stress/"},
                {'type': 'stress', 'title': 'How to manage and reduce stress', 'description': 'How stress can effect your daily life, what causes it, and how we can manage it', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-manage-and-reduce-stress"},
                
                {'type': 'stress', 'title': 'Coping with Stress', 'description': 'NHS guide on how to manage stress, including practical tips and symptoms.', 'logo': 'logos/nhs_thumbnail.png', 'url': 'https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/dealing-with-stress/', 'is_recommended': True},
                {'type': 'stress', 'title': 'Stress Management Tips', 'description': 'Mental Health Foundation’s strategies to reduce stress and improve resilience.', 'logo': 'logos/mental_health_foundation.png', 'url': 'https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/stress', 'is_recommended': True},

                {'type': 'anxiety', 'title': 'Anxiety and panic attacks', 'description': 'Explains anxiety and panic attacks, including possible causes and how you can access treatment and support. Includes tips for helping yourself, and guidance for friends and family.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety-and-panic-attacks/self-care/"},
                {'type': 'anxiety', 'title': 'Managing anxiety', 'description': 'What causes anxiety and tips on we can manage it', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/anxiety/"},
                {'type': 'anxiety', 'title': 'Anxiety', 'description': 'This content discusses anxiety, panic attacks, loneliness or isolation, trauma and substance abuse or addiction (which may include mentions of alcohol or drug use), which some people may find triggering.', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/anxiety"},
                {'type': 'anxiety', 'title': 'Anxiety disorders', 'description': 'This article details different kinds of anxiety disorders, their causes and how we can handle them in our daily lives', 'logo': 'logos/rethink_mental_illness.png', 'url': "https://www.rethink.org/advice-and-information/about-mental-illness/mental-health-conditions/anxiety-disorders/"},
                
                {'type': 'anxiety', 'title': 'Anxiety UK Support Services', 'description': 'Access self-help resources, therapy, and support for various anxiety conditions.', 'logo': 'logos/anxiety.png', 'url': 'https://www.anxietyuk.org.uk/', 'is_recommended': True},
                {'type': 'anxiety', 'title': 'Anxiety Self-Help Guide', 'description': 'NHS step-by-step self-help guide for managing generalised anxiety.', 'logo': 'logos/nhs_thumbnail.png', 'url': 'https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder/self-help/', 'is_recommended': True},

                {'type': 'depression', 'title': 'Low mood', 'description': 'Difference between a low mood and depression, and top tips on how to improve your mood', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/low-mood/"},
                {'type': 'depression', 'title': 'Depression - treatment and management', 'description': 'Types of depression, treatment, coping and recovering', 'logo': 'logos/better_health.png', 'url': "https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/depression-treatment-and-management"},
                {'type': 'depression', 'title': 'Depression', 'description': 'This section explains the causes and symptoms of depression and how it is treated.', 'logo': 'logos/rethink_mental_illness.png', 'url': "https://www.rethink.org/advice-and-information/about-mental-illness/mental-health-conditions/depression/"},
                
                {'type': 'depression', 'title': 'Understanding Depression', 'description': 'Mind’s overview of depression symptoms, treatments, and getting support.', 'logo': 'logos/mind.png', 'url': 'https://www.mind.org.uk/information-support/types-of-mental-health-problems/depression/', 'is_recommended': True},
                {'type': 'depression', 'title': 'Depression Self-Help Guide', 'description': 'Free NHS self-help guide with exercises for managing low mood and depression.', 'logo': 'logos/nhs_thumbnail.png', 'url': 'https://www.nhs.uk/mental-health/conditions/clinical-depression/self-help/', 'is_recommended': True},
                
                {'type': 'self-esteem', 'title': 'What is self-esteem?', 'description': 'Self-esteem is how we value and perceive ourselves. It is based on our opinions and beliefs about ourselves, which can feel difficult to change. We might also think of this as self-confidence.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/self-esteem/about-self-esteem/"},
                {'type': 'self-esteem', 'title': 'How can I improve my self-esteem?', 'description': 'This page has some tips and suggestions for improving your self-esteem, or self-confidence.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/self-esteem/tips-to-improve-your-self-esteem/"},
                {'type': 'self-esteem', 'title': 'Recovery and mental illness', 'description': 'Recovery and mental illness means different things to different people. On this page, we focus on personal recovery.', 'logo': 'logos/rethink_mental_illness.png', 'url': "https://www.rethink.org/advice-and-information/living-with-mental-illness/treatment-and-support/recovery-and-mental-illness/"},
                {'type': 'self-esteem', 'title': 'Self-care', 'description': 'What self-care really means, and how it can work for you', 'logo': 'logos/youngminds.png', 'url': "https://www.youngminds.org.uk/young-person/coping-with-life/self-care/"},
                
                {'type': 'self-esteem', 'title': 'Improving Self-Esteem', 'description': 'NHS tips for building confidence and addressing low self-worth.', 'logo': 'logos/nhs_thumbnail.png', 'url': 'https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/improve-your-self-esteem/', 'is_recommended': True},
                {'type': 'self-esteem', 'title': 'Low Self-Esteem Explained', 'description': 'YoungMinds article on how low self-esteem can affect young people and how to get help.', 'logo': 'logos/yonugminds.png', 'url': 'https://www.youngminds.org.uk/young-person/mental-health-conditions/self-esteem/', 'is_recommended': True},
                
                {'type': 'sleep', 'title': 'Improve your sleep', 'description': 'Your sleep is affected by what you do throughout your day. Following these tips will put you in a better position to get restful sleep.', 'logo': 'logos/student_space.png', 'url': "https://studentspace.org.uk/wellbeing/improve-your-sleep"},
                {'type': 'sleep', 'title': 'How to fall asleep faster and sleep better', 'description': 'If you are having trouble sleeping, knowing how to sleep better can make a big difference. On this page you will find practical tips to help you to build good sleep hygiene and sleep better.', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/how-to-fall-asleep-faster-and-sleep-better/"},
                {'type': 'sleep', 'title': 'Sleep problems', 'description': 'Advice for common sleep problems, sleep disorders and treatments', 'logo': 'logos/youngminds.png', 'url': "https://www.youngminds.org.uk/young-person/my-feelings/sleep-problems/"},
                {'type': 'sleep', 'title': 'The Impact Of Sleep On Health And Wellbeing', 'description': 'The aim of this report is to raise awareness about the importance of sleep and its crucial role for our health, both physical and mental, just like diet and exercise.', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/sleep-matters-impact-sleep-health-and-wellbeing"},
                {'type': 'sleep', 'title': 'How to sleep better', 'description': 'This guide offers tips on how to sleep better - looking at improving the quality of your sleep, what causes sleep disorders and possible solutions', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-sleep-better"},
    
                {'type': 'sleep', 'title': 'Sleep and Mental Health', 'description': 'Mental Health Foundation’s insights on how poor sleep affects wellbeing and how to improve it.', 'logo': 'logos/mental_health_foundation.png', 'url': 'https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/sleep', 'is_recommended': True},
                {'type': 'sleep', 'title': 'Tips for Better Sleep', 'description': 'Mind’s guide on sleep problems and practical advice to improve sleep hygiene.', 'logo': 'logos/mind.png', 'url': 'https://www.mind.org.uk/information-support/types-of-mental-health-problems/sleep-problems/tips-to-improve-your-sleep/', 'is_recommended': True},
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

    for r in resources:
        resource = Resource(**r)
        db.session.add(resource)

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
    u.forms_completed=2
    u.best_category='anxiety'
    u.worst_category='stress'

    u = db.session.get(User, 12)
    u.forms_completed = 1
    u.best_category = 'stress'
    u.worst_category = 'depression'

    u = db.session.get(User, 13)
    u.forms_completed = 1
    u.best_category = 'self-esteem'
    u.worst_category = 'stress'

    u = db.session.get(User, 14)
    u.forms_completed = 1
    u.best_category = 'depression'
    u.worst_category = 'self-esteem'

    u = db.session.get(User, 15)
    u.forms_completed = 1
    u.best_category = 'depression'
    u.worst_category = 'anxiety'

    u = db.session.get(User, 16)
    u.forms_completed = 1
    u.best_category = 'depression'
    u.worst_category = 'stress'

    u = db.session.get(User, 17)
    u.forms_completed = 1
    u.best_category = 'anxiety'
    u.worst_category = 'self-esteem'




    db.session.commit()
