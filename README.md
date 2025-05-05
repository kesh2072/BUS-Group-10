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
- Please add more here!

## Implemented Core Functionalities

- Dynamic Webpage
  - Feature description here


- Personalised Forms
  - Feature description here
  

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
