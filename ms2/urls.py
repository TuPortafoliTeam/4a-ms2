from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ms2App.views import *

from ms2App.views.coverCreateView import CoverCreateView
from ms2App.views.coverDeleteView import CoverDeleteView
from ms2App.views.coverUpdateView import CoverUpdateView
from ms2App.views.coverDetailView import CoverDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/detail/<int:pk>', SkillsDetailView.as_view()),
    path('skills/create', SkillsCreateView.as_view()),
    path('skills/update/<int:pk>', SkillsUpdateView.as_view()),
    path('skills/delete/<int:pk>', SkillsDeleteView.as_view()),
    path('ms2App/', include('ms2App.urls')),
    path('perfil/<int:pk>', PerfilRUDView.as_view()),
    path('perfil', PerfilCreateView.as_view()),
    path('perfilEmpresa/<int:pk>', PerfilEmpresaRUDView.as_view()),
    path('perfilEmpresa', PerfilEmpresaCreateView.as_view()),
    path('cover/detail/<int:pk>', CoverDetailView.as_view()),
    path('cover/create', CoverCreateView.as_view()),
    path('cover/update/<int:pk>', CoverUpdateView.as_view()),
    path('cover/delete/<int:pk>', CoverDeleteView.as_view()),
]
