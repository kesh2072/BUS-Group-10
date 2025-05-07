from flask import render_template, redirect, url_for, flash, request
from app import app
from app.models import User, Student, Question, Answer, Resource, VisibleStudent
from app.forms import ChooseForm, LoginForm, QuestionForm, ChangePasswordForm, ChangeUniDetails
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
from app.processor import MLQuestionProcessingManager
from sqlalchemy import func, desc
from datetime import datetime
from matplotlib.figure import Figure
import base64
from io import BytesIO
from app.debug_utils import populate
from app.form_management import FormManagement # singleton class to keep track of when forms were rolled out to know when to send reminders
from app import mail
from flask_mail import Message


def apply_anonymity(students):
    new_students = []
    for stu in students:
        if not stu.anonymous:
            stu = VisibleStudent(stu)
        new_students.append(stu)
    return new_students


@app.route('/delete_user', methods=['POST'])
def delete_user():
    form = ChooseForm()
    if form.validate_on_submit():
        u = db.session.get(User, int(form.choice.data))
        q = db.select(User).where((User.role == "Admin") & (User.uid != u.uid))
        first = db.session.scalars(q).first()
        if not first:
            flash("You can't delete your own account if there are no other admin users!", "danger")
        elif u.uid == current_user.uid:
            logout_user()
            db.session.delete(u)
            db.session.commit()
            flash("User deleted", "success")
            return redirect(url_for('home'))
        else:
            db.session.delete(u)
            db.session.commit()
            flash("User deleted", "success")
    return redirect(url_for('admin'))


@app.route("/")
def home():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    if current_user.role == "Student":
        return redirect(url_for('student'))
    if current_user.role == "Staff":
        return redirect(url_for('staff'))
    if current_user.role == "Admin":
        return redirect(url_for('admin'))
    return render_template('home.html',title="Home")


@app.route("/student")
@login_required
def student():
    student = db.session.scalar(
                sa.select(User).where(User.uid == current_user.uid))
    student = VisibleStudent(student)
    student_attr = student.display_attributes()
    resources = Resource.query.filter_by(is_recommended=False).all()
    recommended_resources = Resource.query.filter_by(is_recommended=True)
    return render_template('student.html', title="Student", student_attr=student_attr, resources=resources, recommended_resources=recommended_resources)


@app.route("/staff")
@login_required
def staff():
    instance_of_form_management = FormManagement()
    released = instance_of_form_management.released
    return render_template('staff.html', title="Staff", released = released)


@app.route("/admin")
@login_required
def admin():
    if current_user.role != "Admin":
        return redirect(url_for('home'))
    form = ChooseForm()
    q = db.select(User).where((User.role == "Staff"))
    staff = db.session.scalars(q)
    b = db.select(Student)
    students = db.session.scalars(b)
    anonymity_applied_students = apply_anonymity(students)
    students_attrs = [s.display_attributes() for s in anonymity_applied_students]
    return render_template('admin.html', title="Admin", staff=staff, form=form, students_attrs=students_attrs)


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
        current_user.username = form.username.data
        current_user.name = form.name.data
        current_user.university_email = form.university_email.data
        db.session.commit()
        flash('University details updated successfully', 'success')
        return redirect(url_for('home'))
    return render_template('generic_form.html', title='Change Student Details', form=form)


@app.route('/question_form', methods=['GET', 'POST'])
def question_form():
    instance_of_form_management = FormManagement()
    if instance_of_form_management.release_date:
        released = True
    else:
        released = False
    instance_of_processor = MLQuestionProcessingManager()
    q_list = instance_of_processor.question_generator(current_user)
    form = QuestionForm(q_list=q_list)
    questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
    for i, qi in enumerate(questions):
        getattr(form, qi).label.text = q_list[i].text + ' (' + q_list[i].label + ')'

        if form.validate_on_submit():
            timestamp = datetime.now()
            flash('Thank you for submitting the questionnaire', 'success')

            all_answers = current_user.answers
            form_numbers = [ans.form_number for ans in all_answers]
            if form_numbers:
                form_number = max(form_numbers) + 1
            else:
                form_number = 1

            for i in range(10):
                current_user.answers.append(
                    Answer(content=request.form.get(questions[i]), form_number=form_number, qid=q_list[i].qid,
                           submission_date=timestamp))
            current_user.answers.append(
                Answer(content=request.form.get('q11'), form_number=form_number, qid=q_list[10].qid, type="Text Answer",
                       submission_date=timestamp))
            current_user.forms_completed += 1

            worst, best = instance_of_processor.worst_best(current_user)
            current_user.best_category = best
            current_user.worst_category = worst
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('question_form.html', title='Question Form', form=form, released=released)


@app.route("/staff/view_students", methods=["GET", "POST"])
@login_required
def view_students():
    form=ChooseForm()
    q = db.select(Student)
    students = db.session.scalars(q)
    anonymity_applied_students = apply_anonymity(students)
    students_attrs = [s.display_attributes() for s in anonymity_applied_students]
    flagged_students = []
    for student in students_attrs:
        if student["flagged"]:
            flagged_students.append(student)
    return render_template('view_students.html', title="View all students", flagged_students=flagged_students, students_attrs=students_attrs, form=form)


@app.route("/staff/remove_anonymity", methods=["GET", "POST"])
@login_required
def remove_anonymity():
    uid = request.args.get("uid")
    q = db.select(Student).where(Student.uid == int(uid))
    student = db.session.scalar(q)
    student.anonymous = False
    db.session.commit()
    flash(f"Anonymity removed for student {student.uid}", "success")
    return redirect(url_for('view_student', id=uid))


@app.route("/staff/remove_flag", methods=["GET", "POST"])
def remove_flag():
    uid = request.args.get("uid")
    q = db.select(Student).where(Student.uid == int(uid))
    student = db.session.scalar(q)
    student.flagged = False
    db.session.commit()
    flash(f"Flag removed for student {student.uid}", "success")
    return redirect(url_for('view_student', id=uid))


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

    if not student.anonymous:
        student = VisibleStudent(student)
    student_attr = student.display_attributes()

    recent_response = []
    if answers_by_submission:
        recent_response = list(answers_by_submission.values())[0][10].content

    return render_template('view_student.html', title="View Student", student_attr=student_attr, answers_by_submission=dict(answers_by_submission), recent_response=recent_response)


@app.route("/staff/statistics", methods=["GET", "POST"])
@login_required
def statistics():
    # Retrieve the worst category from all students
    q = (
        db.select(Student.worst_category, func.count().label("count"))
        .where(Student.worst_category.isnot(None))
        .group_by(Student.worst_category)
        .order_by(desc("count"))
    )
    result = db.session.execute(q).first()
    most_common_category = ""
    amount = ""
    if result:
        most_common_category = result[0]
        amount = result[1]

    avg_per_type = (
    db.session.query(
        Question.label.label("type"),
        func.round(func.avg(Answer.content), 2).label("average")
    )
    .join(Answer, Answer.qid == Question.qid)
    .group_by(Question.label)
    .order_by(desc("average"))
    .all()
    )

    # Bar chart for different categories
    categories = []
    amount_of_students = []
    for k in (db.session.execute(q)):
        categories.append(k[0])
        amount_of_students.append(k[1])

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

    return render_template('statistics.html', title="Statistics", most_common_category=most_common_category, amount=amount, priority_list=priority_list, data=data, avg_per_type=avg_per_type)


@app.route('/release_forms', methods = ['GET', 'POST'])
def release_forms():
    populate()
    instance_of_form_management = FormManagement()
    instance_of_form_management.set_release_date()
    flash('Students will now have two weeks to fill out the form', 'success')
    return redirect(url_for('home'))


@app.route('/send_reminders', methods = ['GET', 'POST'])
def send_reminders():
    instance_of_form_management = FormManagement()
    late_students = instance_of_form_management.late_students()
    if late_students:
        email_list = [late_student.university_email for late_student in late_students]
        message = Message(subject = 'Form Reminder', sender = 'testuserformreminder@gmail.com', recipients = email_list)
        message.body = 'Hi! This is a reminder to fill out the wellbeing questionnaire.'
        mail.send(message)
        flash('Emails have been sent out to students who are not up to date on their forms.', 'success')
    else:
        flash('All students are up to date on their forms', 'success')
    return redirect(url_for('staff'))


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
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


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