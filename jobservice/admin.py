from django.contrib import admin
from . models import JobOffer
from . models import Cv
from . models import ReplyToOffer
from . models import FeedbackAnswer
from . models import Company
from . models import Person

# Register your models here.
admin.site.register(JobOffer)
admin.site.register(Cv)
admin.site.register(ReplyToOffer)
admin.site.register(FeedbackAnswer)
admin.site.register(Company)
admin.site.register(Person)
