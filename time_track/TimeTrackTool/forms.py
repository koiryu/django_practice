from django import forms
from .models import Task

class MyForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['TaskName', 'TimeStart', 'TimeEnd']
    """
    Number = forms.IntegerField(label="Number")
    TaskName = forms.CharField(label="TaskName")
    TimeStart = forms.TimeField(label="TimeStart")
    TimeEnd = forms.TimeField(label="TimeEnd")
    """
