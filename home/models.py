from django.db import models

# Create your models here.

class Tasks(models.Model):
    task = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due = models.DateField(auto_now=False)