from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('about/', views.about, name='about-job'),
    path('accounts/profile/',views.profile, name='profile'),
    path('accounts/create/',views.create, name='create'),
]
