# smartnotes

This Django application, named smartnotes, provides a simple and user-friendly interface for creating and managing tasks with due dates. Users can easily create tasks, specify due dates, and delete tasks when they are completed. The application is designed to be easily integrated into existing Django projects or used as a standalone application.

Features
Task Creation: Users can create tasks by providing a task name and selecting a due date.
Due Date Selection: When creating a task, users can choose a due date from a date picker.
Task Deletion: Completed tasks can be deleted from the system.

Installation
Install the TaskManager app by running the following command:
pip install django-smartnotes

Add 'smartnotes' to your INSTALLED_APPS in your Django project settings:
# settings.py

INSTALLED_APPS = [
    # ...
    'smartnotes',
    # ...
]

Run migrations to create the necessary database tables:
python manage.py migrate

Usage
1. Create a Task
To create a task, follow these steps:

Log in to the admin interface (/admin) and navigate to the "SmartNotes" section.
Click on the "Add Task" button.
Enter the task name and select a due date from the date picker.
Click "Save" to create the task.
2. Delete a Task
To delete a task, follow these steps:

Log in to the admin interface (/admin) and navigate to the "SmartNotes" section.
Select the task you want to delete.
Click on the "Delete" button and confirm the deletion.
