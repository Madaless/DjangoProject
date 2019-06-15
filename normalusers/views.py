from django.shortcuts import render, redirect
from .forms import (PersonRegisterForm, PersonUpdateForm) 
from django.contrib import messages
from . import models
from django.contrib.auth.decorators import login_required
from companyusers.decorators import (company_required, person_required)
from django.urls import reverse


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = PersonRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = PersonRegisterForm()
    return render(request, 'normalusers/register.html', {'form': form})

# @login_required
# @person_required
def editperson(request):
    if request.method == 'POST':
        form = PersonUpdateForm(request.POST, instance=request.user.person)

        if form.is_valid():
            form.save()
            return redirect(reverse('profileuser'))
    else:
        form = PersonUpdateForm(instance=request.user.person)
        args = {'form': form}
        return render(request, 'normalusers/editperson.html', args)

