from django import forms
from .models import Cv, JobOffer, ReplyToOffer, FeedbackAnswer

class Cv_form(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('nameCv', 'lastName', 'firstName', 'dateOfBirth', 'education', 'placeOfResidence', 'experience', 'description')


class Offer_form(forms.ModelForm):

    class Meta:
        model = JobOffer
        fields = ('title','trade','proffesion','jobPosition','location','additionalSkills','additionalInfo')


# class ReplyToOffer_form(forms.ModelForm):

#     class Meta:
#         model = ReplyToOffer
#         fields = ('idPerson','idOffer','dateAdd','cv','messForCompany')


# class FeedbackAnswer_form(forms.ModelForm):

#     class Meta:
#         model = FeedbackAnswer
#         fields = ('idReplyToOffer','accept','response')