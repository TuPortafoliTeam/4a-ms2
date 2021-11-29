from django.contrib import admin
from django.urls import path
from ms2App.views import *

urlpatterns = [
    path('perfil/<int:pk>', PerfilRUDView.as_view()),
    path('perfil', PerfilCreateView.as_view()),
]
