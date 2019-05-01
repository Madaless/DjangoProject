from django.shortcuts import render
from django.http import HttpResponse
from .models import JobOffer
# Create your views here.

# joboffers = [
#     {
#         'author' :  'Samsung',
#         'title' : '.net developer with english',
#         'content' : 'Szukamu kogos kto ..',
#         'postdate' : '5 Sierpien 2016',
#     },
#      {
#         'author' :  'Software xd',
#         'title' : 'scala senior developer ',
#         'content' : 'Szukamu kogos kto x..',
#         'postdate' : '5 Sierpien 2018',
#     },
#     {
#         'author' :  'Facebook',
#         'title' : 'php engenier',
#         'content' : 'Szukamu kogos kto x..',
#         'postdate' : '9 Sierpien 2018',
#     },
#     {
#         'author' :  'NK',
#         'title' : 'html engenier',
#         'content' : 'Szukamu kogos kto x..',
#         'postdate' : '18 Sierpien 2018',
#     },
#     {
#         'author' :  'Youmi',
#         'title' : 'project manager',
#         'content' : 'Szukamu kogos kto x..',
#         'postdate' : '18 Sierpien 2018',
#     }
# ]

def home(request):
    context = {
        'joboffers' : JobOffer.objects.all()
    }
    return render(request,'jobservice/home.html', context)

def about(request):
    return render(request,'jobservice/about.html',{'title':'About'})