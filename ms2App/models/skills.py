from djongo import models


class Skills(models.Model):
    idSkills = models.ObjectIdField()
    nombre = models.CharField(max_length=50, null=True)
    experiencia = models.CharField(max_length=500, null=True)
    dominio = models.CharField(max_length=500, null=True)
    usuario = models.IntegerField()
