from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
#from django.conf import settings


# Create your models here.

class User(AbstractUser):
    is_person = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, default="")
    userName = models.CharField(max_length=10,default="")
    personMail = models.EmailField(default="")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    creationdate = models.DateTimeField(auto_now_add=True)
    lastName = models.CharField(max_length=20,blank=True)
    firstName = models.CharField(max_length=10,blank=True)
    age = models.CharField(max_length=50,blank=True)
    

    def __str__(self):
        return self.userName

class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    companyName = models.CharField(max_length= 50,default="")
    companyMail = models.EmailField(default="")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    aboutUs = models.TextField(blank=True)
    site = models.CharField(max_length= 50,default="",blank=True)
    location = models.CharField(max_length= 50,default="",blank=True)
    
    def __str__(self):
        return self.companyName

class JobOffer(models.Model):
    salary = models.CharField(max_length=10,default="",blank=True)
    title = models.CharField(max_length= 50,default="")
    industry = models.CharField(max_length= 50,default="",blank=True)
    proffesion = models.CharField(max_length= 50,default="",blank=True)
    jobPosition = models.CharField(max_length= 50,default="",blank=True)
    jobType = models.CharField(max_length= 50,default="",blank=True)
    ExperienceLevel = models.CharField(max_length= 50,default="",blank=True)
    postdate = models.DateTimeField(default=timezone.now)
    companyName = models.ForeignKey(Company, on_delete = models.CASCADE)
    location =  models.CharField(max_length=300,default="")
    jobDescription = models.TextField(max_length=300,default="",blank=True)



    def __str__(self):
        return self.title+' '+str(self.companyName)

    def get_absolute_url(self):
        return reverse('offer-details', kwargs={'pk': self.pk})

class Cv(models.Model):
    
    person = models.ForeignKey(Person, on_delete = models.CASCADE,default="")
    nameCv = models.CharField(max_length=50,blank=True,default="cv")
    lastName = models.CharField(max_length=50,blank=True)
    firstName = models.CharField(max_length=50,blank=True)
    dateOfBirth = models.CharField(max_length=50,blank=True)
    education = models.TextField(max_length=300,blank=True)
    placeOfResidence = models.TextField(max_length=300,blank=True)
    experience = models.TextField(max_length=300,blank=True)
    description = models.TextField(max_length=300,blank=True)

    def __str__(self):
        return self.nameCv


class ReplyToOffer(models.Model):
    idPerson = models.ForeignKey(Person, on_delete = models.CASCADE,default="")
    idOffer = models.ForeignKey(JobOffer, on_delete = models.CASCADE,default="")
    dateAdd = models.DateTimeField(auto_now_add=True)
    cv = models.ForeignKey(Cv, on_delete = models.CASCADE, default="")
    messForCompany = models.TextField(max_length=150,default="",blank=True)
    link = models.TextField(max_length=150,default="",blank=True)

    def __str__(self):
        return str(self.idOffer)+' '+str(self.idPerson)

class FeedbackAnswer(models.Model):
    idReplyToOffer = models.ForeignKey(ReplyToOffer, on_delete = models.CASCADE,default="")
    response = models.TextField(max_length=300, default="")

    def __str__(self):
        return str(self.idReplyToOffer)+' '+str(self.response)

