from . models import Todo_list
from django import forms
class Todoedit(forms.ModelForm):
    class Meta:
        model=Todo_list
        fields=['task_name','date','priority','desc']
