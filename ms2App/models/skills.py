from django.db import models

class Skills(models.Model):
    idSkills=models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=50, null=True)
    experiencia=models.CharField(max_length=500,null=True)
    dominio=models.CharField(max_length=500,null=True)
    usuario=models.CharField(max_length=40,null=True)