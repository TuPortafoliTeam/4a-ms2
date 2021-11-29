from django import forms
from djongo import models


class Tecnologia (models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    version = models.CharField(max_length=100)

    class Meta:
        managed = False


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = (
            'nombre', 'version'
        )


class Duracion (models.Model):
    inicio = models.CharField(max_length=2000, primary_key=True)
    fin = models.CharField(max_length=2000)

    class Meta:
        managed = False


class DuracionForm(forms.ModelForm):
    class Meta:
        model = Duracion
        fields = (
            'inicio', 'fin'
        )


class Enlaces (models.Model):
    enlace = models.CharField(max_length=2000, primary_key=True)

    class Meta:
        managed = False


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
    usuario = models.IntegerField()
    objects = models.DjongoManager
