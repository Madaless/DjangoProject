from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jobservice.models import (Company, User, Person)
from django.db import transaction

class PersonRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_person = True
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['image']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['image']