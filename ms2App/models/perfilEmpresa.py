from django.db import models

class perfilEmpresa(models.Model):
    
    idPerfilEmpresa= models.BigAutoField(primary_key=True)
    sector = models.CharField(max_length=50)
    vacantes = models.CharField(max_length=200)
    calificacion = models.IntegerField()
    añoCreacion = models.TimeField
    Usuario = models.CharField(max_length=50)