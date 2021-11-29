from django.db import models


class Cover(models.Model):
    idCover = models.BigAutoField(primary_key=True)
    idUsuario = models.IntegerField()
    trabajo = models.CharField(max_length=500, null=True)
    contenido = models.TextField()
