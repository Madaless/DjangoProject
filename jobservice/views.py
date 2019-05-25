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

from .forms import Cv_form
from . models import JobOffer, Company, Person, Cv
from . import models
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

# def start(request):
#     return render(request,'jobservice/start.html',{'title':'start'})


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
    return render(request,'normalusers/profileuser.html',{'title':'Profil'})

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
    


#     
# #@method_decorator([login_required, company_required], name='dispatch')
# # @login_required
# # @company_required
# # def createoffer(request):
# #     if request.method == "POST":
# #         form = Offer_form(request.POST)
# #         offer.companyName = request.user
# #         offer.postdate = timezone.now()
#         if form.is_valid():
#             offer.save()
#             url = 'offer/' + str(offer.offer_id) 
#             return redirect(url)
#         return render(request,'companyusers/createoffer.html',{'form':form})
#     else:
#         form = Offer_form()
#         return render(request,'companyusers/createoffer.html',{'form':form})

# def cv(request, cv_id):
#     response = "You're looking at cv: %s."
#     return HttpResponse(response % cv_id)

def offer(request, offer_id):
    p = JobOffer.objects.all()
    return render(request,'jobservice/offer.html',{'offerts':p})

def companyview(request, company_id):
    p = Company.objects.all()
    return render(request,'companyusers/companyview.html',{'companies':p})

# def personview(request, person_id):
#     p=Person.objects.get(person_id=person_id)
#     return render(request,'companyusers/createoffer.html',{'form':form})







# def create_cv(request):
#     if request.method == 'POST':
#         name = request.POST['CVNewName']
#         nowe_cv = models.Cv.objects.create(nameCv=name, person=request.user)
#         # return redirect('cv', cv_id = cv.cv_id)
#         url = 'cv/' + str(cv.cv_id) 
#         return redirect(url)
#     else:
#         nowe = Cv_form()
#         return render(request,'normalusers/create_cv.html',{'form': nowe })


def cv(request, cv_id):
    person = Person.objects.get(user=request.user)
    p = Cv.objects.filter(Person = person)
    return render(request,'normaluser/cv.html',{'cvs':p})