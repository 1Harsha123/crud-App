from django import forms
from .models import Stu

class StudentForm(forms.ModelForm):
    class Meta:
        model = Stu
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
