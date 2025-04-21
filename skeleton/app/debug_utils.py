from app import db
from app.models import User, Student, Question, Answer

def reset_db():
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

    for u in users:
        user = User(**u)
        user.set_password("PASSWORD")
        db.session.add(user)

    for s in students:
        student = Student(**s)
        student.set_password("PASSWORD")
        db.session.add(student)

    db.session.commit()
