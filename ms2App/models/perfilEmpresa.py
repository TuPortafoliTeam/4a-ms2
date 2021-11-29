from djongo import models


class Vacante(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    requerimientos = models.TextField()

    class Meta:
        managed = False


class PerfilEmpresa(models.Model):
    sector = models.CharField(max_length=50)
    vacantes = models.ArrayField(model_container=Vacante)
    calificacion = models.IntegerField()
    anioCreacion = models.CharField(max_length=4)
    usuario = models.IntegerField(primary_key=True)
