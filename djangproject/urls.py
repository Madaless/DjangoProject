"""djangproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from companyusers import views as companyusers_views
from jobservice import views as jobservice_views
from django.contrib.auth import views as auth_views
from normalusers import views as normalusers_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobservice.urls')),
    #path('register/', companyusers_views.register, name='register'  ),
    path('login/', auth_views.LoginView.as_view(template_name = 'companyusers/login.html'), name='login'  ),
    path('logout/', jobservice_views.mylogout, name = 'logout'),
    path('signup/', companyusers_views.signup, name='signup'),
    path('signup/company/', companyusers_views.register, name='company_signup'),
    path('signup/person/', normalusers_views.register, name='person_signup'),

]