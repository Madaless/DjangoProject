from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('about/', views.about, name='about-job'),
    path('start/', views.start, name='start'),
    path('profilecompany/', views.profilecompany, name='profilecompany'),
    path('profileuser/', views.profileuser, name='profileuser'),
    path('createcv/', views.createcv, name='createcv'),
    path('createoffer/', views.createoffer, name='createoffer'),
    path('offer/<int:offer_id>/', views.offer, name='offer'),
    path('cv/<int:cv_id>/', views.cv, name='cv'),
    
]
