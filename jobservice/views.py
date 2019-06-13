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
from django.conf import settings
# from le_site.models import *
import smtplib

# Create your views here

def emailS(request, email_id):
    subject = 'FindJob'
    em = FeedbackAnswer.objects.get(pk=email_id)
    r=ReplyToOffer.objects.get(pk=r.idReplyToOffer)
    message = em.response
    email_from = settings.EMAIL_HOST_USER
    recipient_list =['szprytny14@gmail.com'] #[person.personMail]
    send_mail( subject, message, email_from, recipient_list )
    # r.delete()
    return redirect('')

def emailview(request, email_id):
    ppppp=FeedbackAnswer.objects.filter(pk=email_id)
    return render(request,'jobservice/emailview.html',{'email':ppppp })


def email(request, reply_id):
    r= ReplyToOffer.objects.get(pk=reply_id)
    if request.method == "POST":
        message = request.POST.get('response','')
        # r= ReplyToOffer.objects.get(pk=reply_id)
        # offer = r.idOffer
        # print(offer)
        # person = r.idPerson
        # print(person)
        ojj=FeedbackAnswer.objects.create(idReplyToOffer=r, response=message)
        ojj.save()
        return redirect('emailview', email_id=ojj.pk)
    else:
        form = ReplyToOffer_form()
        return render(request,'jobservice/email.html',{'form':form, 'rr':r })

# def answer(request, reply_id):
#     r= ReplyToOffer.objects.get(pk=reply_id)
#     if request.method == "POST":
#         rr = request.POST.get('response','')
#         a = request.POST.get('accept','')
#         oj=FeedbackAnswer.objects.create(idReplyToOffer=r, Response=rr, Accept=a)
#         oj.save()
#         return redirect('jobservice/answerview.html', pk=oj.pk)
#     else:
#         form = FeedbackAnswer_form()
#     return render (request, 'jobservice/answer.html',{'answer': form, 'reply': r } )

# def answerview(request, answer_id):
#     ppppp=FeedbackAnswer.objects.filter(pk=answer_id)
#     return render(request,'jobservice/answerview.html',{'answers':ppppp })

    # if request.method == "POST":
    #     message = request.POST.get('response','')
    #     print(message)
    #     # message = 'Siemanko z projektu. Odpalaj blanta dziwko'
    #     # subject = 'FindJob'
    #     # email_from = settings.EMAIL_HOST_USER
    #     r= ReplyToOffer.objects.get(pk=reply_id)
    #     offer = r.idOffer
    #     person = r.idPerson
    #     ojj=FeedbackAnswer.objects.create(idReplyToOffer=r.pk, response=message)

    #     print(ojj)

    #     # recipient_list =['szprytny14@gmail.com'] #[person.personMail]
    #     # send_mail( subject, message, email_from, recipient_list )
    #     # r.delete()
    #     return render(request,'jobservice/welcome.html',{'email':ojj })
    # else:
    #     form = FeedbackAnswer_form()
    #     return render(request,'jobservice/email.html',{'form':form})

    #     # return redirect('jobs-home')
    #     # return redirect('offer-details', offer.pk)

    # # if request.method == "POST":
    # #     form = FeedbackAnswer_form(request.POST)
    # #     if form.is_valid():
    # #         test = form.save(commit=False)
    # #         person = Person.objects.get(user=request.user)
    # #         test.person = person
    # #         test.save()
    # #         return redirect('cv', cv_id = test.pk)
    # #     return  render(request,'normalusers/create_cv.html',{'form':form})
    # # else:
    # #     form = F_form()
    # #     return render(request,'normalusers/create_cv.html',{'form':form})

def mainsite(request):
    return render(request,'jobservice/welcome.html',{'title':'About'})


def home(request):
    queryset_list = JobOffer.objects.all()
    query = request.GET.get("q")
    company = Company.objects.all()
    
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(companyName__companyName__icontains=query)
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
    c = Company.objects.get(user=request.user.company)
    p = JobOffer.objects.filter(companyName = request.user.company)
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
        # form = Cv_form()
        return render(request,'normalusers/create_cv.html',{})#{'form':form})

def offer(request, offer_id):
    p = JobOffer.objects.all()
    print(p)
    pp = ReplyToOffer.objects.get(idOffer=p.pk)
    print(pp)
    return render(request,'jobservice/offer.html',{'offers':p, 'rs':pp })

def companyview(request, company_id):
    cc = Company.objects.get(pk=company_id)
    p = JobOffer.objects.filter(companyName = cc.user.company)
    return render(request,'companyusers/companyview.html',{'companies':cc, 'o':p})

# def personview(request, person_id):
#     p=Person.objects.get(person_id=person_id)
#     return render(request,'companyusers/createoffer.html',{'form':form})
@login_required
@person_required
def cv(request, cv_id):
    p = Cv.objects.filter(pk=cv_id)
    return render(request,'normalusers/cv.html',{'p':p})

@login_required
@person_required
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
        return redirect('replyview', reply_id = oj.pk)
    else:
        form = ReplyToOffer_form()
        return render(request,'jobservice/replytooffer.html',{'form':form, 'offers': a, 'cvs':c })
@login_required
@person_required
def replyview(request, reply_id):
    # pp = JobOffer.objects.get(pk=reply_id)
    p = ReplyToOffer.objects.filter(pk=reply_id)
    # c = Cv.objects.get(pk=p.cv.pk)
    # if  ppp.idOffer.pk == pp.pk:
        # p = ReplyToOffer.objects.filter(pk=reply_id)
    return render(request,'jobservice/replyview.html',{'replys':p })
    # return redirect('offer-details', pk=pk)
@login_required
@person_required   
def deleteCv(request, cv_id): 
    # c=Cv.objects.get(pk = cv_id)
    # if c.person==request.user:
    Cv.objects.get(pk = cv_id).delete()
    return redirect('profileuser')
    # else:
    #     return redirect('cv', pk=cv_id)

<<<<<<< HEAD
# def answer(request, reply_id):
#     r= ReplyToOffer.objects.get(pk=reply_id)
#     if request.method == "POST":
#             rr = request.POST.get('response','')
#             a = request.POST.get('accept','')
#             # oj=FeedbackAnswer.objects.create(idReplyToOffer=r, Response=rr, Accept=a)
#             # oj.save()
#             send_mail('JobOffers', rr, 'from@example.com', ['joan.mk7@gmail.com'], fail_silently=False)
#             return redirect('jobservice/answer.html', pk=reply_id)
#     else:
#         form = FeedbackAnswer_form()
#         return render (request, 'jobservice/answer.html',{'answer': form, 'reply': r } )
    
# def answerview(request, answer_id):
#     ppppp=FeedbackAnswer.objects.filter(pk=answer_id)
#     return render(request,'jobservice/answerview.html',{'answers':ppppp })
=======
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
>>>>>>> 670020189c96da0f6d2c8773b642272062d61504
    

def cvedit(request,cv_id):
    p = Cv.objects.get(pk = cv_id)
    Cv.objects.get(pk = cv_id).delete()
    return render(request,'normalusers/create_cv.html', {'form': p})

@login_required
@person_required
def deleteuser(request):
    u=request.user.delete()
    return redirect('jobs-welcome')

@login_required
@person_required
def editperson(request): #początki początku xD
    u=Person.objects.get(user=request.user)
    return render(request,'normalusers/editperson.html', {'form': u})

@login_required
@company_required
def editcompany(request):
    c=Company.objects.get(user=request.user.company)
    return render (request,'companyusers/editcompany.html', {'form':c})