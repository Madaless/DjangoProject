from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from companyusers.decorators import (company_required, person_required)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



from .forms import Cv_form, Offer_form
from . models import JobOffer
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def start(request):
    return render(request,'jobservice/start.html',{'title':'start'})


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
def createcv(request):
    if request.method == "POST":
        form = Cv_form(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.userName = request.user
            cv.save()
            return redirect('cv', cv_id = cv.cv_id)
        return  render(request,'normalusers/createcv.html',{'form':form})
    else:
        form = Cv_form()
        return render(request,'normalusers/createcv.html',{'form':form})

#@method_decorator([login_required, company_required], name='dispatch')
@login_required
@company_required
def createoffer(request):
    if request.method == "POST":
        form = Offer_form(request.POST)
        offer.companyName = request.user
        offer.postdate = timezone.now()
        if form.is_valid():
            offer.save()
            url = 'offer/' + str(offer.offer_id) 
            return redirect(url)
        return render(request,'companyusers/createoffer.html',{'form':form})
    else:
        form = Offer_form()
        return render(request,'companyusers/createoffer.html',{'form':form})

def cv(request, cv_id):
    response = "You're looking at cv: %s."
    return HttpResponse(response % cv_id)

def offer(request, offer_id):
    response = "You're looking at offer: %s."
    return HttpResponse(response % offer_id)
    # return render(request,'jobservice/joboffer.html',{'title':'offer'})
