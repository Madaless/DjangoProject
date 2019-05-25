from django.urls import path
from . import views
from companyusers.views import (OfferListView, OfferCreateView, OfferDetailView,OfferUpdateView, OfferDeleteView)


urlpatterns = [
    path('', OfferListView.as_view(), name='jobs-home'),
    path('about/', views.about, name='about-job'),
    #path('start/', views.start, name='start'),
    path('profilecompany/', views.profilecompany, name='profilecompany'),
    path('profileuser/', views.profileuser, name='profileuser'),
    path('create_cv/', views.create_cv, name='create_cv'),
    #path('createoffer/', views.createoffer, name='createoffer'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer-details'),
    path('offer/new/', OfferCreateView.as_view(), name='offer-create'),
    path('offer/<int:pk>/update', OfferUpdateView.as_view(), name='offer-update'),
    path('offer/<int:pk>/delete', OfferDeleteView.as_view(), name='offer-delete'),
    path('cv/<int:cv_id>/', views.cv, name='cv'),
    path('company/<int:company_id>/', views.companyview, name='companyview'),
    # path('person/<int:person_id>/', views.personview, name='personview'),
]
 