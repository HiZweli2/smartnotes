from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from . models import Tasks

class TodoForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task','due',)
        labels = {'task':'','due':''}
        widgets = {
            'task': forms.TextInput(attrs={'class':'text'}), 
            'due': forms.widgets.DateInput(attrs={'type': 'date','class':'dateInput'})
            }

