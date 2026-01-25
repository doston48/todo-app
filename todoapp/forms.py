from django import forms 

from .models import todo

class todoform(forms.ModelForm):
    class meta:
        model = todo
        fields = ["title", "description", "priority", "due_date"]