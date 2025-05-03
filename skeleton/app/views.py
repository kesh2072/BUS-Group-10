from flask import render_template, redirect, url_for, flash, request
from app import app
from app.models import User, Student, Question, Answer
from app.forms import ChooseForm, LoginForm, QuestionForm, ChangePasswordForm, ChangeUniDetails
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
from app.processor import MLQuestionProcessingManager
from sqlalchemy import func, desc
from app.anonymity import VisibleStudent
from datetime import datetime
from matplotlib.figure import Figure
import numpy as np
import base64
from io import BytesIO

resources = {
    'stress': [{'label': 'Student stress', 'description': 'Tips on student stress: ways to detect symptoms and handle it better', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/mental-health/children-and-young-adults/help-for-teenagers-young-adults-and-students/student-stress-self-help-tips/"},
               {'label': '5 ways to manage student stress', 'description': 'Tips on handling your stress better as a student', 'logo': 'logos/prospects.png', 'url': "https://www.prospects.ac.uk/applying-for-university/university-life/5-ways-to-manage-student-stress#:~:text=If%20possible%20leave%20your%20stresses,the%20triggers%20of%20your%20stressors."},
               {'label': 'Dealing with stress', 'description': 'Details on what causes stress and how we can better deal with it', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/stress/"},
               {'label': 'How to manage and reduce stress', 'description': 'How stress can effect your daily life, what causes it, and how we can manage it', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-manage-and-reduce-stress"}],
    'anxiety': [{'label': 'Anxiety and panic attacks', 'description': 'Explains anxiety and panic attacks, including possible causes and how you can access treatment and support. Includes tips for helping yourself, and guidance for friends and family.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety-and-panic-attacks/self-care/"},
                {'label': 'Managing anxiety', 'description': 'What causes anxiety and tips on we can manage it', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/anxiety/"},
                {'label': 'Anxiety', 'description': 'This content discusses anxiety, panic attacks, loneliness or isolation, trauma and substance abuse or addiction (which may include mentions of alcohol or drug use), which some people may find triggering.', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/anxiety"},
                {'label': 'Anxiety disorders', 'description': 'This article details different kinds of anxiety disorders, their causes and how we can handle them in our daily lives', 'logo': 'logos/rethink_mental_illnes.png', 'url': "https://www.rethink.org/advice-and-information/about-mental-illness/mental-health-conditions/anxiety-disorders/"}],
    'depression': [{'label': 'Low mood', 'description': 'Difference between a low mood and depression, and top tips on how to improve your mood', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-health-issues/low-mood/"},
                   {'label': 'Depression - treatment and management', 'description': 'Types of depression, treatment, coping and recovering', 'logo': 'logos/better_health.png', 'url': "https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/depression-treatment-and-management"},
                   {'label': 'Depression', 'description': 'This section explains the causes and symptoms of depression and how it is treated.', 'logo': 'logos/rethink_mental_illness.png', 'url': "https://www.rethink.org/advice-and-information/about-mental-illness/mental-health-conditions/depression/"}],
    'self-esteem': [{'label': 'What is self-esteem?', 'description': 'Self-esteem is how we value and perceive ourselves. It is based on our opinions and beliefs about ourselves, which can feel difficult to change. We might also think of this as self-confidence.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/self-esteem/about-self-esteem/"},
                    {'label': 'How can I improve my self-esteem?', 'description': 'This page has some tips and suggestions for improving your self-esteem, or self-confidence.', 'logo': 'logos/mind.png', 'url': "https://www.mind.org.uk/information-support/types-of-mental-health-problems/self-esteem/tips-to-improve-your-self-esteem/"},
                    {'label': 'Recovery and mental illness', 'description': 'Recovery and mental illness means different things to different people. On this page, we focus on personal recovery.', 'logo': 'logos/rethink_mental_illness.png', 'url': "https://www.rethink.org/advice-and-information/living-with-mental-illness/treatment-and-support/recovery-and-mental-illness/"},
                    {'label': 'Self-care', 'description': 'What self-care really means, and how it can work for you', 'logo': 'logos/youngminds.png', 'url': "https://www.youngminds.org.uk/young-person/coping-with-life/self-care/"}],
    'sleep': [{'label': 'Improve your sleep', 'description': 'Your sleep is affected by what you do throughout your day. Following these tips will put you in a better position to get restful sleep.', 'logo': 'logos/student_space.png', 'url': "https://studentspace.org.uk/wellbeing/improve-your-sleep"},
              {'label': 'How to fall asleep faster and sleep better', 'description': 'If you are having trouble sleeping, knowing how to sleep better can make a big difference. On this page you will find practical tips to help you to build good sleep hygiene and sleep better.', 'logo': 'logos/nhs_thumbnail.png', 'url': "https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/how-to-fall-asleep-faster-and-sleep-better/"},
              {'label': 'Sleep problems', 'description': 'Advice for common sleep problems, sleep disorders and treatments', 'logo': 'logos/youngminds.png', 'url': "https://www.youngminds.org.uk/young-person/my-feelings/sleep-problems/"},
              {'label': 'The Impact Of Sleep On Health And Wellbeing', 'description': 'The aim of this report is to raise awareness about the importance of sleep and its crucial role for our health, both physical and mental, just like diet and exercise.', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/sleep-matters-impact-sleep-health-and-wellbeing"},
              {'label': 'How to sleep better', 'description': 'This guide offers tips on how to sleep better - looking at improving the quality of your sleep, what causes sleep disorders and possible solutions', 'logo': 'logos/mental_health_foundation.png', 'url': "https://www.mentalhealth.org.uk/explore-mental-health/publications/how-sleep-better"}],
}

@app.route("/")
def home():
    return render_template('home.html',title="Home")


@app.route("/admin")
@login_required
def admin():
    if current_user.role != "Admin":
        return redirect(url_for('home'))
    form = ChooseForm()
    q = db.select(User)
    user_lst = db.session.scalars(q)
    return render_template('admin.html', title="Admin", user_lst=user_lst, form=form)


@app.route("/staff")
@login_required
def staff():
    return render_template('staff.html', title="Staff")


@app.route('/change_pw', methods=['GET', 'POST'])
@login_required
def change_pw():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Password changed successfully', 'success')
        return redirect(url_for('home'))
    return render_template('generic_form.html', title='Change Student Password', form=form)

@app.route('/change_uni_details', methods=['GET', 'POST'])
@login_required
def change_uni_details():
    form = ChangeUniDetails()
    if form.validate_on_submit():
        student_details = Student(username=form.username.data,
                                  email=form.university_email.data,
                                  name=form.name.data,
                                  student_id=form.student_id.data)
        db.session.update(student_details)
        db.session.commit()
        flash('University Details Updated successfully', 'success')
        return redirect(url_for('home'))
    return render_template('generic_form.html', title='Change Student Details', form=form)

def apply_anonymity(students):
    new_students = []
    for stu in students:
        if not stu.anonymous:
            stu = VisibleStudent(stu)
        new_students.append(stu)
    print(new_students)
    return new_students

@app.route("/staff/view_students", methods=["GET", "POST"])
@login_required
def view_students():
    form=ChooseForm()
    q = db.select(Student)
    students = db.session.scalars(q)
    anonymity_appplied_students = apply_anonymity(students)
    students_attrs = [s.display_attributes() for s in anonymity_appplied_students]
    return render_template('view_students.html', title="View all students", students_attrs=students_attrs, form=form)

@app.route("/staff/toggle_anonymity", methods=["GET", "POST"])
@login_required
def toggle_anonymity():
    form = ChooseForm()
    if form.validate_on_submit():
        student = db.session.get(Student, int(form.choice.data))
        student.anonymous = False if student.anonymous == True else True
        db.session.commit()
    return redirect(url_for('view_students'))

@app.route("/staff/student/<int:id>")
@login_required
def view_student(id):
    student = db.session.get(Student, id)
    answers_by_submission = {}
    for answer in student.answers:
        
        if answer.submission_date not in answers_by_submission:
            answers_by_submission[answer.submission_date] = []
        
        answers_by_submission[answer.submission_date].append(answer)

    answers_by_submission = dict(sorted(answers_by_submission.items(), reverse=True))

    if student.anonymous == False:
        student = VisibleStudent(student)

    student_attr = student.display_attributes()

    return render_template('view_student.html', title="View Student", student_attr=student_attr, answers_by_submission=dict(answers_by_submission))

@app.route("/staff/statistics", methods=["GET", "POST"])
@login_required
def statistics():
    # Retrieve worst category from all students
    q = (
        db.select(Student.worst_category, func.count().label("count"))
        .where(Student.worst_category.isnot(None))
        .group_by(Student.worst_category)
        .order_by(desc("count"))
    )
    result = db.session.execute(q).first()
    most_common_category = result[0]
    amount = result[1]

    # Bar chart for different categories
    categories = []
    amount_of_students = []
    for k in (db.session.execute(q)):
        categories.append(k[0])
        amount_of_students.append(k[1])
    
    print(categories)
    print(amount_of_students)

    fig = Figure()
    ax = fig.subplots()
    ax.bar(categories, amount_of_students)
    ax.set_title("Distribution of 'worst categories' for students")
    ax.set_xlabel('Categories')
    ax.set_ylabel('Amount of Students')

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    # Retrieve average grade for each student
    # This still gets average over ALL past questionnaires
    list_averages = (
    db.select(Student.uid, Student.name, func.round(func.avg(Answer.content), 2).label("average"))
    .join(Answer, Answer.uid == Student.uid)
    .group_by(Student.uid)
    .order_by(desc('average'))
    )

    priority_list = db.session.execute(list_averages).all()

    return render_template('statistics.html', title="Statistics", most_common_category=most_common_category, amount=amount, priority_list=priority_list, data=data)


@app.route("/student")
@login_required
def student():
    student = db.session.scalar(
                sa.select(User).where(User.uid == current_user.uid))
    student = VisibleStudent(student)
    student_attr = student.display_attributes()
    return render_template('student.html', title="Student", student_attr=student_attr, resources=resources)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('generic_form.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/question_form', methods = ['GET', 'POST'])
def question_form():
    instance_of_processor = MLQuestionProcessingManager()
    q_list=instance_of_processor.QG(current_user)
    form = QuestionForm(q_list=q_list)
    questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
    for i,qi in enumerate(questions):
        getattr(form,qi).label.text= q_list[i].text + ' ('+ q_list[i].label +')'


    if form.validate_on_submit():
        timestamp = datetime.now()
        flash('Thank you for submitting the questionnaire', 'success')

        all_answers = current_user.answers
        form_numbers = [ans.form_number for ans in all_answers]
        if form_numbers:
            form_number = max(form_numbers) + 1
        else:
            form_number = 1
        # qid doesn't increase incrementally but needs to correlate with the questions asked
        for i in range(10):
            current_user.answers.append(Answer(content = request.form.get(questions[i]), form_number =form_number, qid =q_list[i].qid, submission_date=timestamp))
        current_user.answers.append(Answer(content = request.form.get('q11'), form_number = form_number, qid = q_list[10].qid, type = "Text Answer", submission_date = timestamp))
        current_user.forms_completed+=1

        worst,best = instance_of_processor.worst_best(current_user)
        current_user.best_category=best
        current_user.worst_category=worst
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('question_form.html', title = 'Question Form', form = form)


# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error'), 403


# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error'), 404


@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error'), 413


# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error'), 500