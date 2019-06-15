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
        email = user.email
        company = Company.objects.create(user=user,companyName = user, companyMail = email)
        company.companyName = user.username
        company.companyName = user.email
        return user

class CompanyAddOfferForm(forms.Form):
    class Meta:
        model = JobOffer
        fields = ['title', 'industry', 'proffesion' ,'jobPosition', 'jobType', 'ExperienceLevel', 'postdate', 'location', 'jobDescription','salary']

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['companyMail','aboutUs', 'site','location']