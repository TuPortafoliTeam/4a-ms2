from typing import Dict
from django import forms
from django.db.models import fields
from  djongo import models



class Tecnologia (models.Model):
    nombre = models.CharField(max_length= 100)
    version = models.CharField(max_length= 100)

    class Meta:
        abstract = True

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = (
            'nombre', 'version'
        )

class Duracion (models.Model):
    inicio = models.CharField(max_length=2000)
    fin = models.CharField(max_length=2000)

    class Meta:
        abstract = True

class DuracionForm(forms.ModelForm):
    class Meta:
        model = Duracion
        fields = (
            'inicio', 'fin'
        )
class Enlaces (models.Model):
    enlace = models.CharField(max_length=2000)

    class Meta:
        abstract = True

class EnlacesForm(forms.ModelForm):
    class Meta:
        model = Enlaces
        fields = (
            'enlace',
        )
class Proyectos (models.Model):
    nombreProyecto = models.CharField(max_length=300)
    tecnologiasUsadas = models.ArrayField(
        model_container=Tecnologia,
        model_form_class=TecnologiaForm
    )
    tematica = models.CharField(max_length=300)
    duracion = models.EmbeddedField(
        model_container=Duracion,
        model_form_class=DuracionForm
    )
    descripcionProyecto = models.CharField(max_length=2000)
    enlaces = models.ArrayField(
        model_container=Enlaces,
        model_form_class=EnlacesForm
    )
    usuario = models.CharField(max_length=300)
    objects = models.DjongoManager