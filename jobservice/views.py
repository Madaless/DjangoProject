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

from .forms import Cv_form, ReplyToOffer_form, FeedbackAnswer_form
from . models import JobOffer, Company, Person, Cv, ReplyToOffer, FeedbackAnswer, User
from . import models
# Create your views here

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def about(request):
    return render(request,'jobservice/about.html',{'title':'About'})

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
    return render(request,'normalusers/profileuser.html',{'cvs':p, 'person':person})

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

def reply(request, pk): #nie działa :c ale wyswietlanie wygląda git
    person = Person.objects.get(user=request.user)
    cvs= Cv.objects.filter(person=person)
    if request.method == "POST":
        form = ReplyToOffer_form(request.POST)        
        cv_id = request.POST.get('cv','3')    #zmianić – tymczasowo     
        cv_id=int(cv_id, base=10)
        c=Cv.objects.get(pk=cv_id)
        j=JobOffer.objects.get(pk=pk)        
        oj=ReplyToOffer.objects.create(idPerson=person, idOffer=j, dateAdd=timezone.now(), cv=c, messForCompany="XD")
        oj.save()
        return redirect('offer-details', pk=pk)
    else:
        form = ReplyToOffer_form()
        return render(request,'jobservice/replytooffer.html',{'form':form, 'cv_id':pk, 'cvs':cvs })

def replyview(request, pk, reply_id):
    pp = JobOffer.objects.get(pk=pk)
    ppp = ReplyToOffer.objects.get(pk=reply_id)
    if  ppp.idOffer.pk == pp.pk:
        p = ReplyToOffer.objects.filter(pk=reply_id)
        return render(request,'jobservice/replyview.html',{'reply':p, 'offer':pp, 'r':ppp })
    return redirect('offer-details', pk=pk)
    
def deleteCv(request,cv_id):
    Cv.objects.get(pk = cv_id).delete()
    return redirect('profileuser')

def answer(request, pk, reply_id):
    if request.method == "POST":
        form = ReplyToOffer_form(request.POST)  
        rr=request.POST.get('reply','5')
        rr=int(rr,base=10)
        id_re=ReplyToOffer.objects.get(reply_id=rr)
        oj=FeedbackAnswer.objects.create(idReplyToOffer=id_re)
        oj.save()
        return redirect('answer',pk=id_re.idOffer.pk, reply_id=id_re.pk)
    else:
        form = FeedbackAnswer_form()
        return render (request, 'jobservice/replyview.html',{'answer': form} )
    


def cvedit(request,cv_id): #poprawić
    p = Cv.objects.get(pk = cv_id)
    return render(request,'normalusers/profileuser.html', {'cvs': p})