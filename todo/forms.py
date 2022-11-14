from django import forms
from django.forms import ModelForm


from .models import Task


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ("name", "deadline", "tags")
        widgets = {
            'deadline': DateTimeInput(),
        }




