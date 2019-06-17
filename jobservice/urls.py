from django.urls import path
from . import views
from companyusers.views import (OfferListView, OfferCreateView, OfferDetailView,OfferUpdateView, OfferDeleteView, editcompany)
from normalusers.views import editperson
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('editperson/', editperson, name='editperson'),
    path('editcompany/', editcompany, name='editcompany'),
    # path('answer/<int:answer_id>/', views.answerview, name='answerview'),
    path('reply/<int:reply_id>/email/', views.email, name='email'),
    path('email/<int:email_id>/emailS', views.emailS, name='emailS'),
    path('email/<int:email_id>/', views.emailview, name='emailview'),
    path('offer/<int:pk>/sendreply/', views.sendreply, name='sendreply'),
    path('reply/<int:reply_id>/', views.replyview, name='replyview'),
    path('offer/<int:pk>/reply/', views.reply, name='reply'),
    path('offer/<int:pk>/update', OfferUpdateView.as_view(), name='offer-update'),
    path('offer/<int:pk>/delete', OfferDeleteView.as_view(), name='offer-delete'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer-details'),
    path('offer/new/', OfferCreateView.as_view(), name='offer-create'),
    path('company/<int:company_id>/', views.companyview, name='companyview'),
    path('profilecompany/', views.profilecompany, name='profilecompany'),
    path('profileuser/', views.profileuser, name='profileuser'),
    path('create_cv/', views.create_cv, name='create_cv'),
    path('cv/<int:cv_id>/', views.cv, name='cv'),
    path('cv/<int:cv_id>/delete', views.deleteCv, name='deletecv'),
    path('cv/<int:cv_id>/edit', views.cvedit, name='cvedit'),
    path('about/', views.about, name='about-job'),
    path('', views.mainsite, name='jobs-welcome'),
    path('welcome/', views.home, name='jobs-home')
]
 
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)