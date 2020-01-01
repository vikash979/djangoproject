from django import forms
from myapps.models import Student


class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    file = forms.FileField()