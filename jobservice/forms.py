from django import forms
from django.contrib.auth.models import Cv

class Cv(forms.Form):
    nameCv = forms.CharField(max_length=50)
    userName = forms.OneToOneField(Person, on_delete = models.CASCADE)
    lastName = forms.CharField(max_length=50)
    firstName = forms.CharField(max_length=50)
    dateOfBirth = forms.CharField(max_length=50)
    education = forms.CharField(max_length=300)
    placeOfResidence = forms.CharField(max_length=300)
    experience = forms.CharField(max_length=300)
    description = forms.CharField(max_length=300)