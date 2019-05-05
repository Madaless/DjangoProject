from django.shortcuts import render
from django.http import HttpResponse
from .models import JobOffer
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def profile(request):
    return render(request,'jobservice/profile.html',{'title':'Profil'})

def about(request):
    return render(request,'jobservice/about.html',{'title':'About'})
    
def cv(request):
    return render(request,'jobservice/cv.html',{'title':'CV'})