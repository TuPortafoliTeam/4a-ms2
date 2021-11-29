from djongo import models


class Cover(models.Model):
    idCover = models.ObjectIdField()
    idUsuario = models.IntegerField()
    trabajo = models.CharField(max_length=500, null=True)
    contenido = models.TextField()
