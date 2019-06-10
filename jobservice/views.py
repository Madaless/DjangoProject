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
from . models import JobOffer, Company, Person, Cv, ReplyToOffer, FeedbackAnswer, JobOffer
from . import models
from django.core.paginator import Paginator
from django.db.models import Q

from django.core.mail import send_mail

# Create your views here



def mainsite(request):
    return render(request,'jobservice/welcome.html',{'title':'About'})


def home(request):
    queryset_list = JobOffer.objects.all()
    query = request.GET.get("q")
    company = Company.objects.all()
    
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) #|
           # Q(company__companyName__name=query)
            ).distinct()
    
    paginator = Paginator(queryset_list, 10) # Show 10 per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    queryset_list = paginator.get_page(page)
    context = {
        'joboffers' : queryset_list
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
    c = Company.objects.get(user=request.user)
    p = JobOffer.objects.filter(companyName = request.user)
    return render(request,'companyusers/profilecompany.html',{'company': c , 'off': p })

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
    print(p)
    pp = ReplyToOffer.objects.get(idOffer=p.pk)
    print(pp)
    return render(request,'jobservice/offer.html',{'offers':p, 'rs':pp })

def companyview(request, company_id):
    cc = Company.objects.get(pk=company_id)
    p = JobOffer.objects.filter(companyName = cc.user)
    return render(request,'companyusers/companyview.html',{'companies':cc, 'o':p})

# def personview(request, person_id):
#     p=Person.objects.get(person_id=person_id)
#     return render(request,'companyusers/createoffer.html',{'form':form})

def cv(request, cv_id):
    p = Cv.objects.filter(pk=cv_id)
    return render(request,'normalusers/cv.html',{'p':p})

def reply(request, pk): 
    a = JobOffer.objects.get(pk=pk)
    print(a)
    per = Person.objects.get(user=request.user)
    c= Cv.objects.filter(person= per)
    j= JobOffer.objects.get(pk=pk)
    if request.method == "POST":
        m = request.POST.get('messForCompany','')
        o = request.POST.get('cv','')
        cccccc = Cv.objects.get(pk=o)
        print(m)
        oj=ReplyToOffer.objects.create(idOffer=j, idPerson=per, dateAdd=timezone.now(), cv=cccccc, messForCompany=m)
        oj.save()
        # return redirect('jobs-home')
        return redirect('replyview', reply_id = pk)
    else:
        form = ReplyToOffer_form()
        return render(request,'jobservice/replytooffer.html',{'form':form, 'offers': a, 'cvs':c })

def replyview(request, reply_id):
    # pp = JobOffer.objects.get(pk=reply_id)
    p = ReplyToOffer.objects.filter(pk=reply_id)
    # c = Cv.objects.get(pk=p.cv.pk)
    # if  ppp.idOffer.pk == pp.pk:
        # p = ReplyToOffer.objects.filter(pk=reply_id)
    return render(request,'jobservice/replyview.html',{'replys':p })
    # return redirect('offer-details', pk=pk)
    
def deleteCv(request, cv_id): 
    # c=Cv.objects.get(pk = cv_id)
    # if c.person==request.user:
    Cv.objects.get(pk = cv_id).delete()
    return redirect('profileuser')
    # else:
    #     return redirect('cv', pk=cv_id)

def answer(request, reply_id):
    r= ReplyToOffer.objects.get(pk=reply_id)
    if request.method == "POST":
            rr = request.POST.get('response','')
            a = request.POST.get('accept','')
            # oj=FeedbackAnswer.objects.create(idReplyToOffer=r, Response=rr, Accept=a)
            # oj.save()
            send_mail('JobOffers', rr, 'from@example.com', ['joan.mk7@gmail.com'], fail_silently=False)
            return redirect('jobservice/answer.html', pk=reply_id)
    else:
        form = FeedbackAnswer_form()
        return render (request, 'jobservice/answer.html',{'answer': form, 'reply': r } )
    
def answerview(request, answer_id):
    ppppp=FeedbackAnswer.objects.filter(pk=answer_id)
    return render(request,'jobservice/answerview.html',{'answers':ppppp })
    

def cvedit(request,cv_id):
    p = Cv.objects.get(pk = cv_id)
    Cv.objects.get(pk = cv_id).delete()
    return render(request,'normalusers/create_cv.html', {'form': p})

def deleteuser(request):
    u=request.user.delete()
    return redirect('jobs-welcome')