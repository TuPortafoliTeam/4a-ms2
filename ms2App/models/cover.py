from django.db import models

class Cover(models.Model):
    idCover=models.BigAutoField(primary_key=True)
    idUsuario=models.CharField(max_length=40,null=True)
    trabajo=models.CharField(max_length=500,null=True)
    contenido=models.CharField(max_length=500,null=True)