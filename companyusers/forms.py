from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jobservice.models import (Company, User, JobOffer)
from django.db import transaction

class CompanyRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        student = Company.objects.create(user=user)
        return user

class CompanyAddOfferForm(forms.Form):
    class Meta:
        model = JobOffer
        fields = ['title', 'industry', 'proffesion' ,'jobPosition', 'jobType', 'ExperienceLevel', 'postdate', 'companyName', 'location', 'jobDescription' ]

