from django.shortcuts import render, redirect
from .forms import PersonRegisterForm
from django.contrib import messages
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
