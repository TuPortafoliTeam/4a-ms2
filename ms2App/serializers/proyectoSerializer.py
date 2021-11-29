from ms2App.models.proyecto import Proyectos
from rest_framework import serializers

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Proyectos
       fields = '__all__'