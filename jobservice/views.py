from django.shortcuts import render
from django.http import HttpResponse
from .models import JobOffer
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def start(request):
    return render(request,'jobservice/start.html',{'title':'start'})

def profilecompany(request):
    return render(request,'jobservice/profilecompany.html',{'title':'Profil'})

def profileuser(request):
    return render(request,'jobservice/profileuser.html',{'title':'Profil'})

def about(request):
    return render(request,'jobservice/about.html',{'title':'About'})

def createcv(request):
    return render(request,'jobservice/createcv.html',{'title':'createcreate'})

def createoffer(request):
    return render(request,'jobservice/createoffer.html',{'title':'createoffer'})

def cv(request):
    return render(request,'jobservice/joboffer.html',{'title':'cv'})

def offer(request):
    return render(request,'jobservice/joboffer.html',{'title':'offer'})
