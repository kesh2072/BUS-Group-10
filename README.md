# Mental Health Web App

## System Description

The primary purpose of this system is to improve the depersonalised nature of current mental health resources.

Students have access to a personal ‘dynamic’ webpage, which displays mental health resources.
They also have access to questionnaires - forms - which are populated with questions relating to specific areas of mental health.
When a student fills out a form, the MLProcessingManager determines which areas of mental health the student struggles with the most.
The resources on their homepage then change to reflect this.

Wellbeing Staff can use their own webpage to view various statistics relating to the students registered on the website.
They can see which categories students are struggling with the most, and view all students’ previous forms.

Students may choose to be anonymous on this system, so the staff page does not display the names, emails and student IDs of the students who are anonymous.
However, if a student writes in one of their forms something that could make them a risk to themselves or others (for this prototype, we use the word ‘danger’) the MLProcessingManager flags the student.
Staff members will see this, and can choose to remove the student’s anonymity if they deem it necessary.

## Step-by-step Instructions on Running the Project

1. Step 1
2. Step 2
3. Step 3

## Programming Languages, Frameworks and Tools

- Python
- HTML
- Bootstrap 5
- Flask
- SqlAlchemy
- Matplotlib

## Implemented Core Functionalities

- Dynamic Webpage

  - The first run of the student page has no recommended resources, instead students have access to all resources organised through categories.
  - As students fill in forms, their `worst category` and `best category` is stored and used to render the dynamic homepage as additional resources related to their `worst category` are displayed in the `recommended for you` section.
- Statistics Page

  - The statistics page is divided into three sections: the 'overview' tab in which the staff member is able to quickly view the average scores of each of the 5 categories in the form, across all students.
  - Under the 'distribution' tab, we have generated a bar chart using Matplotlib to display the distribution of the worst categories registered by each student.
  - Under the 'priority_list' tab, we have generated a list, ordered by the students which have scored the highest in their previous questionnaires. Students which have an average score of over 4.0 will be tagged 'urgent priority' in the list, and anyone over 3.0 with 'medium priority'. This priority list allows staff members to quickly see the students who are struggling the most, and need more support.
- Personalised Forms

  - Students fill in forms iteratively and their responses are processed by `processor.py` to allow for personalisation of form questions. Each form has 10 Likert scale questions and one text field, which is optional for the student to fill out.
  - All Likert scale questions fall into one of five categories (stress, anxiety, self-esteem, depression, sleep) - and initially all students are presented with two of each type of question. Upon submission, the `weighting()` function will take averages of their scores for each category and the `label_classifer()` function will search for key words if any exist then assign the response to the most related category and assign more weight to this category. This is also where a student may be flagged (see Breaking Anonymity).
  - Using these two functions, the `worst_best()` function will return the categories that the student struggled with most and least. This will update the student's records for `best_category` and `worst_category`, which will be accessed by the Dynamic Webpage functionality. It will also determine the distribution of questions in the student's next form:
  - The question generator function `QG()` will add an extra question for the student's worst category and remove one question for their best category. This continues in an iterative manner, allowing the app to learn from the student's latest form responses and adjust the next set of questions accordingly.
- Email Reminders

  -	Student users gain access to the forms after they are released by a member of wellbeing staff via the “Release Forms” button on the staff page. Once the button has been clicked, the ‘released’ attribute in the instance of the singleton FormManagement() class is changed from False to True. This makes the Question Form page visible to students.
  -	After the forms are released, students are required to fill in a form every two weeks. To demonstrate how this works, this two-week timeframe has been condensed to 30 seconds in the program.
  -	The wellbeing staff have access to a functionality that sends pre-written reminder emails to students who are behind on their forms. After the “Send forms reminder to students” button is clicked, the program finds the students who are behind on their forms using the ‘late_students’ method in the FormManagement() class. It uses this to send a reminder email to the email addresses for these students. A student user with username ‘test user’ and email address "testuserformreminder@outlook.com" has been set up to demonstrate this. This can be logged into with the password ‘BUSGroup10Password’. The emails are sent from the email address "testuserformreminder@gmail.com" with the same password. 
- Breaking Anonymity

  - The student class found in models.py has a method called `display_attributes()` which returns a dictionary of all their attributes.
    This function 'hides' sensitive info including name, username, email and student_id (by default, the attribute `anonymity=False`)
    Some students in our database have the attribute `anonymity=True`, so whenever these students are displayed, they are first passed to the
    `VisibleStudent` decorator, which changes the `display_attributes()` function to reveal these attributes.
  - When the student fills out a form containing the exact word 'danger', the student is flagged (`flagged=True`). This means that on the
    `view_student.html` page (when logged in as a staff member) there is a message prompting a review of the student's last form submission.
    Staff can then choose to dismiss the flag, or remove the student's anonymity (if they are anonymous).

## Contributions

Contribution Percentages are 20% each. Specific work done as follows:

- Luke Gouldson: basic database design, breaking anonymity functionality
- Madoka Miyazaki: processing form submissions for dynamic forms and webpage
- Imogen Greig: student page, admin page, question form layout plus views.py functions
- Keshava Mohamed-Laarbi: frontend design, staff page and statistics
- Bridget Parris: email reminders, small parts of the personalised forms
