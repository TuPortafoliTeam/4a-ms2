"""ms2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
#from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ms2App.views import *
from ms2App.views.skillsCreateView import SkillsCreateView
from ms2App.views.skillsDeleteView import SkillsDeleteView
from ms2App.views.skillsDetailView import SkillsDetailView
from ms2App.views.skillsUpdateView import SkillsUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/detail', SkillsDetailView.as_view()),
    path('skills/create', SkillsCreateView.as_view()),
    path('skills/update', SkillsUpdateView.as_view()),
    path('skills/delete', SkillsDeleteView.as_view()),
    path('ms2App/', include('ms2App.urls'))
]