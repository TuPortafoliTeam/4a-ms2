from djongo import models


class Formacion(models.Model):
    institucion = models.CharField(max_length=200, primary_key=True)
    anio = models.CharField(max_length=4)
    materia = models.CharField(max_length=100)

    class Meta:
        managed = False


class Trabajo(models.Model):
    empresa = models.CharField(max_length=200, primary_key=True)
    cargo = models.CharField(max_length=100)
    funciones = models.TextField()

    class Meta:
        managed = False


class Perfil(models.Model):
    descripcion = models.TextField(null=True, blank=True)
    metodologia = models.TextField(null=True, blank=True)
    formacion = models.ArrayField(
        model_container=Formacion, null=True, blank=True)
    trabajo = models.ArrayField(model_container=Trabajo, null=True, blank=True)
    intereses = models.TextField(null=True, blank=True)
    usuario = models.IntegerField(null=False, blank=False, primary_key=True)
