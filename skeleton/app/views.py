from flask import render_template, redirect, url_for, flash, request
from app import app
from app.models import User, Student, Question, Answer
from app.forms import ChooseForm, LoginForm, QuestionForm, ChangePasswordForm, ChangeUniDetails
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
from app.processor import MLQuestionProcessingManager

from datetime import datetime


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title="Account")


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

@app.route("/staff/view_students")
@login_required
def view_students():
    form=ChooseForm()
    q = db.select(Student)
    students = db.session.scalars(q)
    return render_template('view_students.html', title="View all students", students=students, form=form)

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
    return render_template('view_student.html', title="View Student", student=student, answers_by_submission=dict(answers_by_submission))



@app.route("/student")
@login_required
def student():
    student = db.session.scalar(
                sa.select(User).where(User.uid == current_user.uid))
    return render_template('student.html', title="Student", student = student)


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

        #works out what form number to label the questions
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