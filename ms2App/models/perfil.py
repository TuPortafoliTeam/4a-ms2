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
    descripcion = models.TextField()
    metodologia = models.TextField()
    formacion = models.ArrayField(model_container=Formacion)
    trabajo = models.ArrayField(model_container=Trabajo)
    intereses = models.TextField()
    usuario = models.IntegerField(null=False, blank=False, primary_key=True)
