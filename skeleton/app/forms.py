from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, SelectField, TextAreaField, IntegerField, RadioField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from app import db
from app.models import User, Student
from flask_login import current_user
from app import app


class ChooseForm(FlaskForm):
    choice = HiddenField('Choice')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


def password_policy(form, field):
    message = """A password must be at least 8 characters long, and have an
                uppercase and lowercase letter, a digit, and a character which is
                neither a letter or a digit"""
    if len(field.data) < 8:
        raise ValidationError(message)
    flg_upper = flg_lower = flg_digit = flg_non_let_dig = False
    for ch in field.data:
        flg_upper = flg_upper or ch.isupper()
        flg_lower = flg_lower or ch.islower()
        flg_digit = flg_digit or ch.isdigit()
        flg_non_let_dig = flg_non_let_dig or not ch.isalnum()
    if not (flg_upper and flg_lower and flg_digit and flg_non_let_dig):
        raise ValidationError(message)

class ChangePasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), password_policy])
    confirm = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="Passwords must match")])
    submit = SubmitField('Change_Password')

    def validate_password(form, field):
        if not current_user.check_password(form.password.data):
            raise ValidationError("Incorrect password")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), password_policy])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(form, field):
        q = db.select(User).where(User.username==field.data)
        if db.session.scalar(q):
            raise ValidationError("Username already taken, please choose another")

    def validate_email(form, field):
        q = db.select(User).where(User.email==field.data)
        if db.session.scalar(q):
            raise ValidationError("Email address already taken, please choose another")


class ChangeUniDetails(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    university_email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Change University details')

    def validate_username(form, field):
        q = db.select(User).where(User.username==field.data)
        if db.session.scalar(q):
            raise ValidationError("Username already taken, please choose another")

    def validate_university_email(form, field):
        q = db.select(User).where(User.university_email==field.data)
        if db.session.scalar(q):
            raise ValidationError("Email address already registered to an account,"
                                  " please select another")



class QuestionForm(FlaskForm):
    #added an empty string as the first element of the choices list so that '1' doesn't appear as the default option.
    #they can't choose the empty string as an option tho bc of the DataRequired validator
    q1 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q2 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q3 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q4 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q5 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q6 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q7 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q8 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q9 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    q10 = RadioField(choices = [("1","1") ,("2", "2"),("3", "3"),("4",  "4") , ("5", "5")], validators = [DataRequired()])
    # removed DataRequired()
    q11 = TextAreaField()
    submit = SubmitField('Submit')


# dynamic questions: using QG here only calls it once when the app is loaded then never calls it again
# so user is stuck with the original 11 questions at every iteration.
# instead i made this form initially question-less and then used QG tp add the text to it in views.py
# Since views.py calls QG at each iteration, it updates accordingly.