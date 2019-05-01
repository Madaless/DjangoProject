from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    companyName = models.CharField(max_length= 50,default="")
    companyMail = models.EmailField(default="")
    companyPassword = models.CharField(max_length= 50,default="") 

class JobOffer(models.Model):
    title = models.CharField(max_length= 50,default="")
    trade = models.CharField(max_length= 50,default="")
    proffesion = models.CharField(max_length= 50,default="")
    jobPosition = models.CharField(max_length= 50,default="")
    postdate = models.DateTimeField(auto_now_add=True)
    companyName = models.ForeignKey(Company, on_delete = models.CASCADE)
    location =  models.CharField(max_length=105,default="")
    additionalSkills = models.CharField(max_length=105,default="")

class Person(models.Model):
    userName = models.CharField(max_length=10,default="")
    personMail = models.EmailField(default="")
    personPassword = models.CharField(max_length=10,default="")

class Cv(models.Model):
    userName = models.OneToOneField(Person, on_delete = models.CASCADE)
    lastName = models.CharField(max_length=50,default="")
    firstName = models.CharField(max_length=50,default="")
    dateOfBirth = models.CharField(max_length=50,default="")
    education = models.CharField(max_length=50,default="")
    placeOfResidence = models.CharField(max_length=50,default="")
    experience = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=50,default="")

class ReplyToOffer(models.Model):
    idPerson = models.ForeignKey(Person, on_delete = models.CASCADE,default="")
    idOffer = models.ForeignKey(JobOffer, on_delete = models.CASCADE,default="")
    dateAdd = models.DateTimeField(auto_now_add=True)

class FeedbackAnswer(models.Model):
    accept = models.CharField(max_length=50,default="")
    response = models.CharField(max_length=50,default="")
