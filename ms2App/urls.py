from django.urls import path
from ms2App.views.proyectoView import proyecto_view,proyecto_detail_view

urlpatterns = [
    path ('proyectos/',proyecto_view, name= 'proyectos'),
    path ('proyectos/<int:pk>/', proyecto_detail_view, name= 'proyecto_detail_view')
]