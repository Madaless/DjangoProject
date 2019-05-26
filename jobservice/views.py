from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from companyusers.decorators import (company_required, person_required)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import Cv_form, ReplyToOffer_form
from . models import JobOffer, Company, Person, Cv, ReplyToOffer
from . import models
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def mylogout(request):
    logout(request)
    return render(request,'jobservice/logout.html',{'title':'start'})

@login_required
@company_required
#@method_decorator([login_required, company_required], name='dispatch')
def profilecompany(request):
    return render(request,'companyusers/profilecompany.html',{'title':'Profil'})

@login_required
@person_required
#@method_decorator([login_required, person_required], name='dispatch')
def profileuser(request):
    person = Person.objects.get(user=request.user)
    p = Cv.objects.filter(person = person)
    return render(request,'normalusers/profileuser.html',{'cvs':p})

def about(request):
    return render(request,'jobservice/about.html',{'title':'About'})

@login_required
@person_required
#@method_decorator([login_required, person_required], name='dispatch')
def create_cv(request):
    if request.method == "POST":
        form = Cv_form(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            person = Person.objects.get(user=request.user)
            test.person = person
            test.save()
            return redirect('cv', cv_id = test.pk)
        return  render(request,'normalusers/create_cv.html',{'form':form})
    else:
        form = Cv_form()
        return render(request,'normalusers/create_cv.html',{'form':form})

def offer(request, offer_id):
    p = JobOffer.objects.all()
    return render(request,'jobservice/offer.html',{'offerts':p})

def companyview(request, company_id):
    p = Company.objects.all()
    return render(request,'companyusers/companyview.html',{'companies':p})

# def personview(request, person_id):
#     p=Person.objects.get(person_id=person_id)
#     return render(request,'companyusers/createoffer.html',{'form':form})

def cv(request, cv_id):
    p = Cv.objects.filter(pk=cv_id)
    return render(request,'normalusers/cv.html',{'cvs':p})

def reply(request, offer_id, pk):
    if request.method == "POST":
        form = ReplyToOffer_form(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            person = Person.objects.get(user=request.user)
            test.idPerson = person
            # offer = JobOffer.objects.get(request.JobOffer)
            test.idOffer = JobOffer.objects.get(pk=offer_id)
            test.dateAdd = timezone.now()
            test.save()
            return redirect('offer-details', pk=test.idOffer)
        return  render(request,'replytooffer.html',{'form':form})
    else:
        form = ReplyToOffer_form()
        return render(request,'replytooffer.html',{'form':form})
    
def deleteCv(request,cv_id):
    # person = Person.objects.get(user=request.user)
    # if request.user==Person:
        Cv.objects.get(pk = cv_id).delete()
        return redirect('profileuser')
    # return redirect('profileuser')

# def editCv(request,cv_id):
    # p = Cv.objects.get(pk = cv_id)
    # return render(request,'cvedit', {'cvs': p})