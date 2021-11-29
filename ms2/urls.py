from django.contrib import admin
from django.urls import path
from ms2App.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/detail', SkillsDetailView.as_view()),
    path('skills/create', SkillsCreateView.as_view()),
    path('skills/update', SkillsUpdateView.as_view()),
    path('skills/delete', SkillsDeleteView.as_view()),
    path('perfil/<int:pk>', PerfilRUDView.as_view()),
    path('perfil', PerfilCreateView.as_view())
]
