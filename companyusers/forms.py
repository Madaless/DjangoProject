from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jobservice.models import (Company, User)
from django.db import transaction

class CompanyRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
        return user



