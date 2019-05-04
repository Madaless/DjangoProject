from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('about/', views.about, name='about-job'),
    path('profile/',views.profile, name='profile'),
]
