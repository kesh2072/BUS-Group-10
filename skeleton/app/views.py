from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory
from app import app
from app.models import User, Student, Question, Answer
from app.forms import ChooseForm, LoginForm, QuestionForm
from flask_login import current_user, login_user, logout_user, login_required, fresh_login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
from app.processor import QG

import csv
import io


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


@app.route("/student")
@login_required
def student():
    return render_template('student.html', title="Student")


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
    q_list=QG(current_user)
    form = QuestionForm(q_list=q_list)
    questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
    for i,qi in enumerate(questions):
        getattr(form,qi).label.text= q_list[i].text + ' ('+ q_list[i].label +')'

    if form.validate_on_submit():
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
            current_user.answers.append(Answer(content = request.form.get(questions[i]), form_number =form_number, qid =q_list[i].qid))
        current_user.answers.append(Answer(content = request.form.get('q11'), form_number = form_number, qid = q_list[10].qid, type = "Text Answer"))
        current_user.forms_completed+=1
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